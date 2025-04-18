from textnode import TextNode
from extract_markdown_images import  extract_markdown_images, extract_markdown_links
import re
from textnode import TextType

def split_nodes_link(old_nodes):
    
    node_list = []
    for node in old_nodes:
        text_from_nodes = re.split(r"(\[.*?\]\(.*?\))", node.text)
        for text in text_from_nodes:
            if len(text) > 0 and text[0] == "[" and text[-1] == ")":
                alt_text = re.findall(r"\[(.*?)\]", text)
                url = re.findall(r"\((.*?)\)", text)
                node_list.append(TextNode(alt_text[0], TextType.LINK, url[0] ))
            elif len(text) > 0:
                node_list.append(TextNode(text, TextType.TEXT))
    return node_list

def split_nodes_image(old_nodes):
    
    node_list = []
    for node in old_nodes:
        text_from_nodes = re.split(r"(!\[.*?\]\(.*?\))", node.text)
        for text in text_from_nodes:
            if len(text) > 0 and text[0] == "!" and text[-1] == ")":
                alt_text = re.findall(r"!\[(.*?)\]", text)
                url = re.findall(r"\((.*?)\)", text)
                node_list.append(TextNode(alt_text[0], TextType.IMAGE, url[0] ))
            elif len(text) > 0:
                node_list.append(TextNode(text, TextType.TEXT))
    return node_list