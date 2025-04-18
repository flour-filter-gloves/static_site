import re
from htmlnode import LeafNode , ParentNode
def handle_link(block):
    pattern = r"(^\[.*?\])(\(.*?\))"

    result = re.findall(pattern,  block)
    if result:
        value = result[0][0].replace("[","")
        value = value.replace("]","")
        href = result[0][1].replace("(","")
        href = href.replace(")","")

        return LeafNode(tag="a", value=value.strip() ,props={'href':href.strip()} )
        