from block_to_block_type import BlockType, block_to_block_type
from handle_paragraphs import handle_paragraphs
from handle_quote import handle_qoute
from htmlnode import ParentNode
from image_handler import image_node_handler
from markdown_to_blocks import markdown_to_blocks
from html_node_maker import leaf_header_node_make
from list_handler import ordered_handler, unordered_handler
import re
from handle_code import handle_code_node
from handle_link import handle_link
def markdown_to_html_node(markdown):
    parent_node = ParentNode("div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:

        result = block_to_block_type(block)
        match result:
           
            case BlockType.LINK:
                link_node = handle_link(block)
                parent_node.children.append(link_node)
            case BlockType.IMAGE:
                parent_node.children.append(image_node_handler(block))
            
            case BlockType.QUOTE:
                parent_node.children.append(handle_qoute(block))
            case BlockType.CODE:
                parent_node.children.append(handle_code_node(block))
                
            case BlockType.HEADING:
                parent_node.children.append(leaf_header_node_make(block))
            case BlockType.PARAGRAPH:
                parent_node.children.append(handle_paragraphs(block))
            case BlockType.UNORDERED_LIST:
                unordered_list_node = unordered_handler(block)
                parent_node.children.append(unordered_list_node)
            case BlockType.ORDERED_LIST:
                ordered_list_node = ordered_handler(block)
                parent_node.children.append(ordered_list_node)
                
    return(parent_node)
