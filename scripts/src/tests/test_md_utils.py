import unittest
import os
import shutil
import tempfile  # Add this import at the top

import scripts.src.md_utils as md_utils

class TestMdUtils(unittest.TestCase):

    def setUp(self):
        # Create a random temporary directory with the following structure
        #
        # mkdocs.yml
        # └── docs
        #     ├── dev
        #     │    └── markdown-editing-tools.md
        #     └── images
        #         └── docs
        #             └── dev
        #                 └── m
        #                     └── image1.png

        self.temp_dir = tempfile.mkdtemp()
        # Create a mock mkdocs.yml file
        self.mkdocs_yml_path = os.path.join(self.temp_dir, 'mkdocs.yml')
        with open(self.mkdocs_yml_path, 'w') as f:
            f.write("""
                    site_name: 'My Docs'
                    docs_dir: 'docs'
                    """)
        os.makedirs(os.path.join(self.temp_dir, 'docs/dev'), exist_ok=True)
        os.makedirs(os.path.join(self.temp_dir, 'images/docs/dev/markdown-editing-tools'), exist_ok=True)

        # Define the test image path
        self.test_image_path = os.path.join(self.temp_dir, 'images/docs/dev/markdown-editing-tools/image1.png')
        
        # Create a mock markdown file
        self.test_md_file_path = os.path.join(self.temp_dir, 'docs/dev/markdown-editing-tools.md')
        with open(self.test_md_file_path, 'w') as f:
            f.write("""
                    # Markdown Editing Tools
                    # ![Image](../images/docs/dev/markdown-editing-tools/image1.png)
                    # """)  # Updated image path

        # mock image is contained a dir relative to the test file
        mock_image_src = os.path.join(os.path.dirname(__file__), 'mocks/image1.png')
        # Copy the mock image file to the test directory
        shutil.copyfile(mock_image_src, self.test_image_path)
        # To simulate the behavior that we expect from the user, chdir into the mock project directory and prepare relative paths arguments
        os.chdir(self.temp_dir)
        self.md_file_relative_path = 'docs/dev/markdown-editing-tools.md'
        self.relative_dest_dir = 'docs/new_location'


    def tearDown(self):
        self.output_file = 'tests/mocks/document_imported.md'  # Final output file

    def tearDown(self):
        # Clean up the generated files after tests
        print(f"Test directory: {self.temp_dir}")

    def test_sanity_check(self):
        md_utils.sanity_check(self.md_file_relative_path, self.relative_dest_dir)
    
    def test_move_and_update_md(self):
        md_utils.move_and_update_md(self.md_file_relative_path, self.relative_dest_dir)
        self.assertTrue(os.path.exists(os.path.join(self.temp_dir, 'docs/new_location/markdown-editing-tools.md')))
        self.assertTrue(os.path.exists(os.path.join(self.temp_dir, 'images/docs/new_location/markdown-editing-tools/image1.png')))
        

    # def test_convert_docx_to_md(self):
    #     print(f"Converting {self.docx_file} to {self.pandoc_md_file} using pandoc...")
    #     convert_docx_to_md(self.docx_file, self.pandoc_md_file)
    #     self.assertTrue(os.path.exists(self.pandoc_md_file))

    # def test_extract_pandoc_image_references(self):
    #     convert_docx_to_md(self.docx_file, self.pandoc_md_file)
    #     image_references = extract_pandoc_image_references(self.pandoc_md_file)
    #     self.assertIsInstance(image_references, list)
    #     self.assertTrue(len(image_references) > 0, "Expected at least one image reference, but found none.")

    # def test_replace_gdoc_images(self):
    #     convert_docx_to_md(self.docx_file, self.pandoc_md_file)
    #     image_references = extract_pandoc_image_references(self.pandoc_md_file)
    #     replace_gdoc_images(self.gdoc_file, self.output_file, image_references)
    #     self.assertTrue(os.path.exists(self.output_file))
        

    # def test_clean_base64_references(self):
    #      # Ensure the output file exists before cleaning
    #     if not os.path.exists(self.output_file):
    #         convert_docx_to_md(self.docx_file, self.pandoc_md_file)
    #         image_references = extract_pandoc_image_references(self.pandoc_md_file)
    #         replace_gdoc_images(self.gdoc_file, self.output_file, image_references)

    #     clean_base64_references(self.output_file)
    #     with open(self.output_file, 'r') as file:
    #         content = file.read()
    #         self.assertNotIn('<data:image/png;base64,', content)

    # def test_sanity_check_valid(self):
    #     try:
    #         sanity_check(self.test_md_file, self.test_dest_dir)
    #     except SystemExit as e:
    #         self.fail("sanity_check raised SystemExit unexpectedly!")

    # def test_sanity_check_invalid_absolute_path(self):
    #     with self.assertRaises(SystemExit):
    #         sanity_check(os.path.abspath(self.test_md_file), self.test_dest_dir)

    #     with self.assertRaises(SystemExit):
    #         sanity_check(self.test_md_file, os.path.abspath(self.test_dest_dir))

    # def test_sanity_check_file_not_exist(self):
    #     with self.assertRaises(SystemExit):
    #         sanity_check('non_existent_file.md', self.test_dest_dir)

    # def test_move_and_update_md(self):
    #     move_and_update_md(self.test_md_file, self.test_dest_dir)

    #     # Check if the markdown file has been moved
    #     self.assertTrue(os.path.exists(os.path.join(self.test_dest_dir, 'test_document.md')))

    #     # Check if the image path in the markdown file has been updated
    #     with open(os.path.join(self.test_dest_dir, 'test_document.md'), 'r') as f:
    #         content = f.read()
    #         self.assertIn('![image](img22.png)', content)

if __name__ == '__main__':
    unittest.main()
