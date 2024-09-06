import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        result = node.props_to_html()
        expected = ' class=container id=main'
        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div")
        result = node.props_to_html()
        expected = None
        self.assertEqual(result, expected)

    def test_props_to_html_single(self):
        node = HTMLNode(tag="input", props={"type": "text"})
        result = node.props_to_html()
        expected = ' type=text'
        self.assertEqual(result, expected)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=["child1", "child2"], props={"class": "container", "id": "main"})
        result = node.__repr__()
        expected = "HTMLNode(div, Hello, ['child1', 'child2'], {'class': 'container', 'id': 'main'})"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()