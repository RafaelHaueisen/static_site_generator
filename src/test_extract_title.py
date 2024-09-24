import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_valid_h1_title(self):
        markdown = "# My Title\n\nThis is a paragraph."
        expected_title = "My Title"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_missing_h1_title(self):
        markdown = "## My Subtitle\n\nThis is a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("Please set an h1 title!" in str(context.exception))

    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("Please set an h1 title!" in str(context.exception))

    def test_h1_not_first_block(self):
        markdown = "This is a paragraph.\n# My Title\n"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("Please set an h1 title!" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
