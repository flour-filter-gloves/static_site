import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6
    IMAGE = 7
    LINK = 8


def block_to_block_type(blocks):
    pattern_ordered = r"^(([\d]+)\.\s)"
    pattern_quote =r"(^>)"
    quote = True
    ordered_list = True
    unordered_list = True
    heading = True
    rank = 0

    for line in blocks.split("\n"):
        if re.findall(r"^(\[.*?\])(\(.*?\))", line) != []:
            return BlockType.LINK
        if re.findall(f"(!\[.*?\]\(.*?\))", line) != []:
            return BlockType.IMAGE
    for line in blocks.split("\n"):
        line = line.strip()
        if re.findall(r"^(\d)\.\s" , line) != []:
            rank = int(re.findall(r"^(\d)\.\s", line )[0])
            break
    if blocks[0] == ">":
        return BlockType.QUOTE
    if [] != re.findall(r"[\`]{3}", blocks):
        return BlockType.CODE
    block_split = blocks.split("\n")

    for line in block_split:
        
        line = line.strip()
        if not line:
            continue
        if line:
            if heading and [] == re.findall(r"^([#]{1,6}[\w\d\s\,\.\-\(\)\"\*\,\>]+?)$", line.strip()):

                heading = False
                
            if quote == True and re.findall(pattern_quote,line.strip()) == []:
                quote = False
            if unordered_list == True and not line.startswith("- "):
                unordered_list = False
            if ordered_list and re.findall(pattern_ordered, line.strip()) == []:
                ordered_list = False
            
            if ordered_list:
                rank += 1
    if quote:
        return BlockType.QUOTE
    elif unordered_list:
        return BlockType.UNORDERED_LIST
    elif ordered_list:
        return BlockType.ORDERED_LIST
    elif heading:
        return BlockType.HEADING
    else:
        return BlockType.PARAGRAPH
    
