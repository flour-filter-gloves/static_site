from htmlnode import LeafNode, ParentNode
import re
from text_node_to_html_node import text_node_to_html_node
from text_to_textnode import text_to_textnode
def leaf_header_node_make(block):
    heading_suffix = block.count("#")
    value = re.sub(r"(^#{1,6}\s)","", block)
    children = text_to_textnode(value)
    tag = f"h{heading_suffix}"
    HeadNode = ParentNode(tag=tag, children=[])
    for child in children:
        if child.text != "":
            HeadNode.children.append(text_node_to_html_node(child))
    
    
    return HeadNode