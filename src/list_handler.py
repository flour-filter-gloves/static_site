from htmlnode import ParentNode, LeafNode
from text_to_textnode import text_to_textnode
from text_node_to_html_node import text_node_to_html_node
import re
def unordered_handler(blocks):
    parent_node = ParentNode(tag="ul", children=[])
    block_split = blocks.split("\n")
    for index in range(len(block_split)):
        # Remove leading whitespace and the hyphen
        repl = re.sub(r"^\s*-\s*", "", block_split[index])
        
        if repl.strip():  # Check if repl is not just whitespace
            li_node = ParentNode(tag="li", children=[])
            text = text_to_textnode(repl)
            
            for node in text:
                li_node.children.append(text_node_to_html_node(node))

            
            parent_node.children.append(li_node)
    return parent_node

def ordered_handler(blocks):
    start = 1
    for block in blocks.split("\n"):
        if block:
            start = re.match(r"(\d+)\.\s", block)[1]
            break
    parent_node = ParentNode(tag=f"ol start={start}",children=[])
    for block in blocks.split("\n"):
        
        if block:

            item = re.match(r"^\d*\.\s(.*)?", block)[1]
            text_nodes = text_to_textnode(item)
            li_node = ParentNode(tag="li", children = [])
            
            for text_node in text_nodes:

                html_node = text_node_to_html_node(text_node)
        
                li_node.children.append(html_node)

            parent_node.children.append(li_node)

            
    return parent_node
