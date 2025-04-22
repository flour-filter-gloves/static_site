import re
from htmlnode import LeafNode , ParentNode
def handle_link(block):
    pattern = r"(^\[.*?\])(\(.*?\))"

    result = re.findall(pattern,  block)
    print("result",result)
    if result:
        value = re.findall(r"^\[(.*?)\]",result[0][0])
        
        href = re.findall(r"\((.*?)\)",result[0][1])
        print("href",href)
        print("value",value[0])
        return LeafNode(tag="a", value=value[0].strip() ,props={'href':href[0].strip()} )
        