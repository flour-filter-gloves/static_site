import re
class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f' href="{self.props['href']}" target="{self.props["target"]}"'
    
    def __repr__(self):
        return (f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if self.children is not None:
            raise Exception("A Leaf can not have children")
        if self.tag == " ":
            return str(self.value)
        elif self.tag is None:
            return self.value
        elif self.tag == "img":
            return f"<{self.tag} src=\"{self.props['src']}\" alt=\"{self.props['alt']}\">{self.props['alt']}"
        elif self.tag == 'a':
            return f"<{self.tag} href=\"{self.props['href']}\">{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>".strip()
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        self.value = None

    def to_html(self):
        for child_index in range (len(self.children)):
            if self.children[child_index].value == "":
                del self.children[child_index]
        if self.tag is None:
            raise ValueError("ParentNodes must have  tag")
        if self.children is None:
            raise ValueError("ParentNodes must have children")
        
        result = f"<{self.tag}>"

        for child in self.children:
            result+=child.to_html()
        
        if "ol" in self.tag:
            result+=f"</ol>"
        else:
            result+=f"</{self.tag}>"
        return result
    