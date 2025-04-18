import unittest
from textnode import TextNode
from text_node_to_html_node import text_node_to_html_node,TextType
from htmlnode import LeafNode,ParentNode

class test_leafnode(unittest.TestCase):
    def test_childlessness(self):
        leaf = LeafNode(tag="p",value= "This is a paragraph of text.")
        leaf.children = "string"
        with self.assertRaises(Exception) as context:
            leaf.to_html()

        self.assertEqual(str(context.exception),"A Leaf can not have children")

    def test_novalue(self):
        leaf = LeafNode("p",None)
        with self.assertRaises(Exception) as context:
            leaf.to_html()

        self.assertEqual(str(context.exception), "All leaf nodes must have a value.")


    def test_leaftohtml(self):
        self.assertEqual("<p>This is a paragraph of text.</p>",LeafNode("p", "This is a paragraph of text.").to_html())
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>",LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"}).to_html())

    def test_notag(self):
        self.assertEqual("value", LeafNode(None, "value").to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nochildren(self):
        parent = ParentNode(tag="p",children=None)
        with self.assertRaises(Exception) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNodes must have children" )

    def test_to_html_with_notag(self):
        parent = ParentNode(tag=None,children=    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        with self.assertRaises(Exception) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNodes must have  tag" )

    def test_to_html_with_multiplechildren(self):
        parent = ParentNode(tag="p",children=    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        
        self.assertEqual(parent.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
