
from markdown_to_blocks import markdown_to_blocks
import os
import re
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if re.match(r"^# .*" , block):
             return (block.replace("#","", 1).strip())

    raise Exception("No header detected.")   
