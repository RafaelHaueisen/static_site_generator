import unittest
from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    
    def test_extract_single_image(self):
        text = "Here is an image ![alt text](https://example.com/image.jpg)"
        expected = [("alt text", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "![first image](https://example.com/image1.jpg) ![second image](https://example.com/image2.jpg)"
        expected = [("first image", "https://example.com/image1.jpg"), ("second image", "https://example.com/image2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_image_with_no_alt_text(self):
        text = "Here is an image ![](https://example.com/image.jpg)"
        expected = [("", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_no_images(self):
        text = "This text contains no images"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_single_link(self):
        text = "Here is a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_multiple_links(self):
        text = "[Google](https://google.com) and [GitHub](https://github.com)"
        expected = [("Google", "https://google.com"), ("GitHub", "https://github.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_link_with_special_characters(self):
        text = "Here is a [special link](https://example.com/page?query=123&sort=asc)"
        expected = [("special link", "https://example.com/page?query=123&sort=asc")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_no_links(self):
        text = "This text contains no links"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()
