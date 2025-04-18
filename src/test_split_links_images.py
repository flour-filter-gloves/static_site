from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode,TextType
import unittest

class Test(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
    [
     TextNode("This is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
     TextNode(" and ", TextType.TEXT),
     TextNode(
         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
     ),
    ],new_nodes
        )

    def test_empty_link(self):
        node = TextNode("",TextType.TEXT)
        ret = split_nodes_link([node])
        self.assertListEqual(ret, [])

    def test_empty_image(self):
        node = TextNode("",TextType.TEXT)
        ret = split_nodes_image([node])
        self.assertListEqual(ret, [])