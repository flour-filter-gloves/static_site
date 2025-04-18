from htmlnode import LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from text_to_textnode import text_to_textnode
from image_handler import image_node_handler

def handle_qoute(block):
    new_block = block.replace("> ","")
    
    child_node = ParentNode(tag="blockquote",children=[])
    text_nodes = text_to_textnode(new_block)
    for text_node in text_nodes:
        if text_node:
            node = text_node_to_html_node(text_node)
            if node.tag == 'img':
                node = image_node_handler(node)
            
            child_node.children.append(node)
    return child_node
    