from enum import Enum
from textnode import TextNode
from text_node_to_html_node import TextType
import re
def split_nodes_delimiter_expressions(old_nodes, delimiter, text_type):
    new_nodes = []
    work = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("That is invalid Markdown syntax.")
        work = re.split(f"{re.escape(delimiter)}+[a-zA-Z ]+{re.escape(delimiter)}+",old_nodes[0].text)
        for item in work:
                
            new_nodes.append(TextNode(str(item),TextType.TEXT))
            work = re.findall(f"{re.escape(delimiter)}+[a-zA-Z ]+{re.escape(delimiter)}+",old_nodes[0].text)
        for item in work:
            new_nodes.append(TextNode(item.replace(delimiter,""),text_type))

    return (new_nodes) 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("That is invalid Markdown syntax.")

        text = node.text
        beg = text.find(delimiter)
        end = text.find(delimiter, beg+len(delimiter))
        while beg != -1:
            
                
            if 0 != beg:
                new_nodes.append(TextNode(text[:beg], TextType.TEXT))
            new_nodes.append(TextNode(text[beg+len(delimiter):end],text_type))
            text = text[end+len(delimiter):]
            beg = text.find(delimiter)
            end = text.find(delimiter, beg+len(delimiter))
        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
