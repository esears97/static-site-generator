import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a completely different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node with a url", TextType.NORMAL, "http://google.com")
        node2 = TextNode("This is a text node with a url", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    def test_url_eq(self): 
        node = TextNode("This is a text node with a url", TextType.NORMAL, "http://google.com")
        node2 = TextNode("This is a text node with a url", TextType.NORMAL, "http://google.com")
        self.assertEqual(node,node2)
if __name__ == "__main__":
    unittest.main()
