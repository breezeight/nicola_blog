import mistune
from mistune.renderers.markdown import MarkdownRenderer
import os
import logging
import json

# Set up logging
#logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the Mistune Markdown Renderer https://mistune.lepture.com/en/latest/api.html#mistune.create_markdown
# Markdown renderer explanation: https://mistune.lepture.com/en/latest/renderers.html
# Markdown renderer reference: https://mistune.lepture.com/en/latest/api.html#mistune.Markdown
markdown = mistune.create_markdown(renderer=MarkdownRenderer())

def pretty_print(obj):
    if isinstance(obj, (dict, list)):
        return json.dumps(obj, indent=2)
    return str(obj)

def extract_images_and_links(ast):
    """
    Extract images and links from the given abstract syntax tree (AST).

    This function traverses the AST and collects all image and link nodes.
    It returns two lists: one containing image objects and the other containing link objects.

    Args:
        ast (list): The abstract syntax tree of the markdown content.

    Returns:
        tuple: A tuple containing two lists:
            - images (list): A list of dictionaries, each representing an image with 'src' and 'title' keys.
            - links (list): A list of dictionaries, each representing a link with 'url' and 'title' keys.
    """
    images = []
    links = []

    for node in ast:
        if node['type'] == 'image':
            logger.debug(f"Raw image node: {pretty_print(node)}")
            image_title = ''.join(child['raw'] for child in node['children'] if child['type'] == 'text')
            image_obj = {
                'src': node['attrs'].get('url', ''),
                'title': image_title
            }
            logger.info(f"Image found: {pretty_print(image_obj)}")
            images.append(image_obj)
        elif node['type'] == 'link':
            logger.debug(f"Raw link node: {pretty_print(node)}")
            link_title = ''.join(child['raw'] for child in node['children'] if child['type'] == 'text')
            link_obj = {
                'url': node['attrs'].get('url', ''),
                'title': link_title
            }
            logger.info(f"Link found: {pretty_print(link_obj)}")
            links.append(link_obj)
        elif 'children' in node:
            child_images, child_links = extract_images_and_links(node['children'])
            images.extend(child_images)
            links.extend(child_links)

    return images, links

# check if the image src exists, abs_dir containg the file
def check_image_src_exist(images_array, abs_file):
    """
    Check if the image sources exist in the given markdown file.

    This function verifies the existence of image files referenced in the markdown content.
    It logs a warning message for any broken image links and an info message for valid image links.

    Args:
        images_array (list): A list of dictionaries, each representing an image with 'src' and 'title' keys.
        abs_file (str): The absolute path to the markdown file being checked.

    Returns:
        None
    """
    # Get the directory of the markdown file
    abs_dir = os.path.dirname(abs_file)
    for image in images_array:
        # Construct the full path for the image
        image_abs_path = os.path.join(abs_dir, image['src'])
        #print("image_abs_path: " + image_abs_path)
        if not os.path.isfile(image_abs_path):
            logger.warning(f"Broken image: {image['src']} in file: {abs_dir}")
        else:
            logger.info(f"Image exists: {image['src']}")

def check_md_file(md_file_path):
    """
    Check a single markdown file for internal links and images.

    Args:
        md_file_path (str): The path to the markdown file to check.
    """
    abs_file = os.path.abspath(md_file_path)

    with open(abs_file, 'r', encoding='utf-8') as md_file:
        logger.info(f"Processing file: {os.path.basename(abs_file)}")
        md_content = md_file.read()
        
        # Parse the Markdown content to AST
        ast = mistune.create_markdown(renderer=None)(md_content)
        
        # Extract images and links
        images, links = extract_images_and_links(ast)
        
        check_image_src_exist(images, abs_file)

def check_md_directory(md_dir):
    """
    Check all markdown files in a directory for internal links and images.

    Args:
        md_dir (str): The path to the directory containing markdown files.
    """
    for root, dirs, files in os.walk(md_dir):
        for file in files:
            if file.endswith('.md'):
                abs_file = os.path.abspath(os.path.join(root, file))
                check_md_file(abs_file)


