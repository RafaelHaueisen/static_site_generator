import unittest
from block_to_block_type import block_to_block_type

class TestMarkdownBlockTypes(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("### Heading 3"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), "code")
        self.assertEqual(block_to_block_type("```\nfunction(){ return 0; }\n```"), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> Another line"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item A\n- Item B"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), "ordered_list")
        self.assertEqual(block_to_block_type("1. Start\n2. Continue\n3. End"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a regular paragraph of text."), "paragraph")
        self.assertEqual(block_to_block_type("Another paragraph with **bold** and *italic* text."), "paragraph")

if __name__ == '__main__':
    unittest.main()
