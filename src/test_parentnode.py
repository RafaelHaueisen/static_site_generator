import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_valid_html_with_multiple_children(self):
        leaf1 = LeafNode(tag="span", value="Child 1")
        leaf2 = LeafNode(tag="span", value="Child 2")
        parent = ParentNode(tag="div", children=[leaf1, leaf2])
        expected = "<div><span>Child 1</span><span>Child 2</span></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_valid_html_with_single_child(self):
        leaf = LeafNode(tag="p", value="Single child")
        parent = ParentNode(tag="div", children=[leaf])
        expected = "<div><p>Single child</p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_no_tag_raises_valueerror(self):
        leaf = LeafNode(tag="p", value="Child")
        parent = ParentNode(children=[leaf])
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no tag")

    def test_no_children_raises_valueerror(self):
        parent = ParentNode(tag="div")
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no children")

    def test_empty_children_list_raises_valueerror(self):
        parent = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no children")

    def test_children_with_invalid_node(self):
        leaf1 = LeafNode(tag="span", value="Child 1")
        invalid_child = "This is not a valid child node"
        parent = ParentNode(tag="div", children=[leaf1, invalid_child])
        with self.assertRaises(AttributeError):
            parent.to_html()

    def test_mixed_children_invalid_and_valid_nodes(self):
        leaf1 = LeafNode(tag="span", value="Child 1")
        invalid_child = "Invalid child"
        parent = ParentNode(tag="div", children=[leaf1, invalid_child])
        with self.assertRaises(AttributeError):
            parent.to_html()

    def test_nested_parent_nodes(self):
        leaf1 = LeafNode(tag="span", value="Nested child")
        child_parent = ParentNode(tag="section", children=[leaf1])
        root_parent = ParentNode(tag="div", children=[child_parent])
        expected = "<div><section><span>Nested child</span></section></div>"
        self.assertEqual(root_parent.to_html(), expected)

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            repr(parent_node),
            "ParentNode(div, [LeafNode(span, child, None)], {'class': 'container'})"
        )

if __name__ == "__main__":
    unittest.main()
