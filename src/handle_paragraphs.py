from htmlnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from text_to_textnode import text_to_textnode
from image_handler import image_node_handler

def handle_paragraphs(block):
    child_node = ParentNode(tag='p',children=[])
    flattened_block = block.replace("\n", " ")
    text_nodes = text_to_textnode(flattened_block)
    
    for text_node in text_nodes:
        if text_node:
            node = text_node_to_html_node(text_node)
            if node.tag == 'img':
                node = image_node_handler(node)
            
            child_node.children.append(node)
    return child_node
