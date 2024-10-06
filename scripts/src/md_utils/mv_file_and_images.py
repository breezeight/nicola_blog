import os
import shutil
import typer
import yaml

def sanity_check(md_src_file_relative_path: str, realtive_dest_dir: str):
    #HACK: check we are in the right directory with some eurustics
    if not os.path.exists('docs') and not os.path.exists('docs/images') and not os.path.exists('mkdocs.yml'):
        typer.echo("You must run this script from the root of the repo")
        raise typer.Exit()

    # Check that the inputs are relative paths
    if os.path.isabs(md_src_file_relative_path) or os.path.isabs(realtive_dest_dir):
        typer.echo("Both the markdown file path and the destination directory must be relative paths.")
        raise typer.Exit()

    # Check that the markdown file exists
    if not os.path.exists(md_src_file_relative_path):
        typer.echo(f"The markdown file {md_src_file_relative_path} does not exist.")
        raise typer.Exit()

    # Create the destination directory if it doesn't exist
    if not os.path.exists(realtive_dest_dir):
        os.makedirs(realtive_dest_dir)

    if not os.path.exists('mkdocs.yml'):
        typer.echo("The current directory does not contain mkdocs.yml")
        raise typer.Exit()
    
    docs_dir = get_docs_dir_from_mkdocs()
    if docs_dir != 'docs':
        typer.echo(f"The docs_dir in mkdocs.yml is set to '{docs_dir}', but it should be 'docs'.")
        raise typer.Exit()


def get_docs_dir_from_mkdocs():
    """
    Extract the docs_dir value from mkdocs.yml using a YAML library.
    """
    docs_dir = 'docs'  # Default value if not specified in mkdocs.yml
    if os.path.exists('mkdocs.yml'):
        with open('mkdocs.yml', 'r') as file:
            mkdocs_config = yaml.safe_load(file)
            docs_dir = mkdocs_config.get('docs_dir', docs_dir)
    return docs_dir


def move_and_update_md(md_src_file_relative_path: str, realtive_dest_dir: str):
    sanity_check(md_src_file_relative_path, realtive_dest_dir)

    # Move the source md fileto the destination directory
    shutil.move(md_src_file_relative_path, realtive_dest_dir)
    
    relative_images_dir = os.path.join('images', os.path.dirname(md_src_file_relative_path), os.path.splitext(os.path.basename(md_src_file_relative_path))[0])
    
    # Move the images directory to the destination directory
    images_realtive_dest_dir = os.path.join('images', realtive_dest_dir)
    print(f"images_realtive_dest_dir: {images_realtive_dest_dir}")
    if not os.path.exists(images_realtive_dest_dir):
        os.makedirs(images_realtive_dest_dir)
    
    shutil.move(relative_images_dir, images_realtive_dest_dir)  # Move the images directory
    
    # # Update the image links in the Markdown file after moving
    # new_md_file_path = os.path.join(realtive_dest_dir, os.path.basename(md_src_file_relative_path))  # Adjust path if necessary
    # with open(new_md_file_path, 'r') as file:
    #     content = file.read()
    
    # # Update the image paths
    # new_image_path = os.path.join(dest_dir, 'img22.png')  # Adjust as necessary
    # updated_content = content.replace('img22.png', os.path.basename(new_image_path))
    
    # with open(new_md_file_path, 'w') as file:
    #     file.write(updated_content)



#app = typer.Typer()

# @app.command()
# def main(md_file: str, dest_dir: str):
#     """Move a file or directory and update the Markdown image links."""
#     move_and_update_md(md_file, dest_dir)
#     typer.echo(f"Moved {md_file} to {dest_dir} and updated {md_file}.")

# if __name__ == "__main__":
#     app()
