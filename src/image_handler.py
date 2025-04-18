from htmlnode import LeafNode, ParentNode
import re
def image_node_handler(text_node):
    pattern = r"^!(\[.*?\])(\(.*?\))"

    result = re.findall(pattern, text_node)
    if result:
    

        
        value = result[0][0].replace("[","")
        value = value.replace("]","")
        href = result[0][1].replace("(","")
        href = href.replace(")","")
        
        return(LeafNode(tag="img", value=value.strip() ,props={'src':href.strip(), 'alt':value.strip()} ))