from generate_page import generate_page_recursivly
from copy_static import copy_static
import os

def main():
    copy_static()
    generate_page_recursivly(from_path= os.path.join(os.getcwd(),"content" ),template_path= os.path.join(os.getcwd(), "template.html"),dest_path= os.path.join(os.getcwd(), "public"),direc_list= os.listdir(os.path.join(os.getcwd(), "content")))

    

main()