import re
def extract_markdown_images(text):
    alt_texts =  re.findall(r"\[(.*?)\]", text)
    links = re.findall(r"\((.+?)\)", text)
    return_list = []
    for index in range(len(links)):
        return_list.append((alt_texts[index],links[index])) 
    return(return_list)

def extract_markdown_links(text):
    alt_texts = re.findall(r"\[(.*?)\]",text )
    links = re.findall(r"\((.+?)\)",text)
    
    return_list = []
    for index in range(len(alt_texts)):
        return_list.append((alt_texts[index], links[index] ))
    return return_list
