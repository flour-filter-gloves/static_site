
def markdown_to_blocks(markdown):

    markdown_lists = markdown.split("\n\n")

    return_list = []
    for mark_down in markdown_lists:
        mark_down = mark_down.strip()
        if mark_down:
            return_list.append("\n".join(list(map(lambda x: x.strip(), mark_down.split("\n")))))
            
    return return_list
