import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_value(self):
        node = LeafNode(tag="span", value="Text")
        result = node.to_html()
        expected = "<span>Text</span>"
        self.assertEqual(result, expected)

    def test_to_html_without_tag(self):
        node = LeafNode(value="Text without tag")
        result = node.to_html()
        expected = "Text without tag"
        self.assertEqual(result, expected)

    def test_to_html_without_value(self):
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_tag_but_empty_value(self):
        node = LeafNode(tag="p", value="")
        result = node.to_html()
        expected = "<p></p>"
        self.assertEqual(result, expected) 
        
    def test_to_html_with_tag_value_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href=https://www.google.com>Click me!</a>'
        self.assertEqual(result, expected)

    def test_repr(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        result = repr(node)
        expected = "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()