from markdown_to_blocks import markdown_to_blocks
import unittest

class TestMarkdownSplitter(unittest.TestCase):
    def test_markdown_with_heading_paragraph_and_list(self):
        input_text = ("# This is a heading\n\n\n\n"
                      "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
                      "* This is the first list item in a list block\n"
                      "* This is a list item\n"
                      "* This is another list item")
        expected_output = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        result = markdown_to_blocks(input_text)
        self.assertEqual(result, expected_output)

    def test_markdown_to_blocks(self):
        input_text = ("This is **bolded** paragraph\n\n"
              "This is another paragraph with *italic* text and `code` here\n"
              "This is the same paragraph on a new line\n\n"
              "* This is a list\n"
              "* with items")
        expected_output = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        result = markdown_to_blocks(input_text)
        self.assertEqual(result, expected_output)

    def test_markdown_to_blocks_newlines(self):
        input_text = ("This is **bolded** paragraph\n\n"
                      "This is another paragraph with *italic* text and `code` here\n"
                      "This is the same paragraph on a new line\n\n"
                      "* This is a list\n"
                      "* with items")
        expected_output = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        result = markdown_to_blocks(input_text)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
