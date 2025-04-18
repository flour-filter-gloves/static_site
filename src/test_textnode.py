import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a not a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_self(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node)

    def test_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    def test_eq_text_type_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node.text_type, node_2.text_type)
if __name__ == "__main__":
    unittest.main()