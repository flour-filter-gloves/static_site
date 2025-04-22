from textnode import TextNode
from extract_markdown_images import  extract_markdown_images, extract_markdown_links
import re
from textnode import TextType
def split_nodes_image(old_nodes):
    
    node_list = []
    for node in old_nodes:
        if node.text == "":
            continue
        text_from_nodes = re.finditer(r"![\[][.\w\d\s]+[\]]\(.*?\)", node.text)
        if re.findall(r"\[(.*?)\]", node.text) == []:
            
            node_list.append(node)
            continue
        if text_from_nodes:
            starting_pos = 0
            for text in text_from_nodes:

                result = re.findall(r"![\[]([\<\-\.\,\w\d\s\"\']+)[\]]\((.*?)\)", text.group())
                if text.span()[0] == starting_pos:

                    node_list.append(TextNode(result[0][0], TextType.IMAGE, result[0][1]) )
                    starting_pos = text.span()[1]
                else:
                    if len(node.text[starting_pos:text.span()[0]]) > 1:
                        node_list.append(TextNode(node.text[starting_pos:text.span()[0]], TextType.TEXT))
                    node_list.append(TextNode(result[0][0], TextType.IMAGE, result[0][1]))
                    starting_pos = text.span()[1]
        if starting_pos < len(node.text):
            node_list.append(TextNode(node.text[starting_pos:], TextType.TEXT))
    return node_list

    
def split_nodes_link(old_nodes):
    
    node_list = []
    for node in old_nodes:
        if node.text == "":
            continue
        text_from_nodes = re.finditer(r"(?<!!)\[[^\]]+\]\([^)]*\)", node.text)
        if re.findall(r"\[(.*?)\]", node.text) == []:
            
            node_list.append(node)
            continue
        if text_from_nodes:
            starting_pos = 0
            for text in text_from_nodes:
                result = re.findall(r"[\[]([\<\-\.\,\w\d\s\"\'\<]+)[\]]\((.*?)\)", text.group())
                if text.span()[0] == starting_pos:
                    node_list.append(TextNode(result[0][0], TextType.LINK, result[0][1]) )
                    starting_pos = text.span()[1]
                else:
                    if len(node.text[starting_pos:text.span()[0]]) > 1:
                        node_list.append(TextNode(node.text[starting_pos:text.span()[0]], TextType.TEXT))
                    if node.text != "":
                        node_list.append(TextNode(result[0][0], TextType.LINK, result[0][1]))
                    starting_pos = text.span()[1]
        if starting_pos < len(node.text):
            
            node_list.append(TextNode(node.text[starting_pos:], TextType.TEXT))
    return node_list