from delimiter import split_nodes_delimiter, split_nodes_delimiter_expressions
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def text_to_textnode(text):
    node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_image(split_nodes_link([node])), "**", TextType.BOLD
            ),
            "_",
            TextType.ITALIC,
        ),
        "`",
        TextType.CODE
    )
    return result