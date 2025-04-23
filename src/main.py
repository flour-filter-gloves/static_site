from generate_page import generate_page_recursivly
from copy_static import copy_static
import os
from sys import argv

def main():
    if len(argv) > 1:
        base_path = argv[1]
    else:
        base_path = "/"
    copy_static()
    generate_page_recursivly(from_path= os.path.join(os.getcwd(),"content" ),template_path= os.path.join(os.getcwd(), "template.html"),dest_path= os.path.join(os.getcwd(), "docs"),direc_list= os.listdir(os.path.join(os.getcwd(), "content")),base_path=base_path)

    

main()