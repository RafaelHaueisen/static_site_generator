import unittest
from textnode import TextNode
from text_to_html_converter import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_text(self):
        text_node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_text_type_bold(self):
        text_node = TextNode("This is bold", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is bold</b>")

    def test_text_type_italic(self):
        text_node = TextNode("This is italic", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is italic</i>")

    def test_text_type_code(self):
        text_node = TextNode("print('Hello World')", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello World')</code>")

    def test_text_type_link(self):
        text_node = TextNode("Click me!", "link", url="https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href=https://www.example.com>Click me!</a>')

    def test_text_type_image(self):
        text_node = TextNode("Image description", "image", url="https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src=https://www.example.com/image.png alt=Image description></img>')

    def test_invalid_text_type(self):
        text_node = TextNode("Invalid type", "unknown")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), 'Text Node type does not exist')

if __name__ == "__main__":
    unittest.main()
