from textnode import TextNode, TextType
import unittest
import delimiter
class test_delimiter(unittest.TestCase):
    def test_bold(self):
        
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = delimiter.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT),
]
        
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        node = TextNode("This is text with a *italicized phrase* in the middle", TextType.TEXT)
        new_nodes = delimiter.split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("italicized phrase", TextType.ITALIC),
    TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    def test_code(self):
        node = TextNode("This is text with a `code phrase` in the middle", TextType.TEXT)
        new_nodes = delimiter.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code phrase", TextType.CODE),
    TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_not_text(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.BOLD)
        new_nodes = delimiter.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [node]
        self.assertEqual(new_nodes, expected)