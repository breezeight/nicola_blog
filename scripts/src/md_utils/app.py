import os
import sys
import typer
# Get the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of 'md_utils' to the Python path
parent_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.insert(0, parent_dir)

from .mv_file_and_images import sanity_check, move_and_update_md
from .sanity_check_internal_links_and_images import check_md_file


app = typer.Typer()

@app.command()
def sanity_check_command(md_src_file_relative_path: str, relative_dest_dir: str):
    """
    Perform a sanity check on the given markdown file and destination directory.
    """
    try:
        sanity_check(md_src_file_relative_path, relative_dest_dir)
        typer.echo("Sanity check passed successfully!")
    except typer.Exit:
        typer.echo("Sanity check failed. Please check the error messages above.")

@app.command()
def move_and_update(md_src_file_relative_path: str, relative_dest_dir: str):
    """
    Move and update the given markdown file to the destination directory.
    """
    try:
        move_and_update_md(md_src_file_relative_path, relative_dest_dir)
        typer.echo(f"Successfully moved and updated {md_src_file_relative_path} to {relative_dest_dir}")
    except Exception as e:
        typer.echo(f"An error occurred: {str(e)}")

@app.command()
def check_links_and_images(dir: str = 'docs'):
    """
    Check internal links and images in the given markdown file.
    """
    check_md_directory(dir)
    typer.echo("Link and image check completed.")

if __name__ == "__main__":
    app()
