from htmlnode import LeafNode , ParentNode

def handle_code_node(block):
    # Remove backticks
    new_block = block.replace("```", "")

    # Trim leading or trailing spaces but preserve literal newlines in content
    new_block = new_block.strip()

    # Ensure trailing newline is preserved
    if not new_block.endswith("\n"):
        new_block += "\n"

    # Wrap in ParentNode and LeafNode
    return ParentNode(tag="pre", children=[LeafNode(tag="code", value=new_block)])

