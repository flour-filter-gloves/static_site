import htmlnode
import unittest

class Test(unittest.TestCase):
    def test_tag(self):
        node_1 = htmlnode.HTMLNode(tag="<p>")
        self.assertEqual(node_1.tag , "<p>")

    def test_props_to_html(self):
        node_1 = htmlnode.HTMLNode(tag="<p>",props=
        {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node_1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_prop_none(self):
        node_1 = htmlnode.HTMLNode()
        self.assertEqual(node_1.tag, None)      
