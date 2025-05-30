import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "this is a test", None, {"name":"Eric", "age":28})
        self.assertEqual(node.props_to_html(), ' name="Eric" age="28"')
    def test_tag(self):
        node = HTMLNode("p", "this is a test", None, {"name":"Eric", "age":28})
        self.assertEqual(node.tag, "p")
    def test_val(self):
        node = HTMLNode("p", "this is a test", None, {"name":"Eric", "age":28})
        self.assertEqual(node.value, "this is a test")
    def test_not_eq(self):
        node = HTMLNode("p", "this is a test", None, {"name":"Eric", "age":28})
        self.assertNotEqual(node.props, {"Name":"hackooooor", "age":69})
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_no_value(self):
        node = LeafNode("p", None, {})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "value cannot be None")
if __name__ == "__main__":
    unittest.main()
