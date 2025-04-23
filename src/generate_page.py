from extract_title import extract_title
from markdown_to_blocks import markdown_to_blocks

from markdown_to_html_node import markdown_to_html_node
import os
import shutil

def generate_page_recursivly(from_path, template_path, dest_path , direc_list = None, base_path=None):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if direc_list:
        
        for direc_or_file in direc_list:
            if os.path.isfile(os.path.join(from_path,direc_or_file)):
                
        

                with open(os.path.join(from_path,"index.md")) as file:
                    markdown = file.read()
                title = extract_title(markdown)
                template_content = markdown_to_html_node(markdown)
                with open(template_path) as template_file:
                    template = template_file.read()
                    template_split = template.split("\n")
                    for line_no in range(len(template_split)):
                        if "{{ Title }}" in template_split[line_no]:
                            title_text = template_split[line_no].replace("{{ Title }}", title)
                            template_split[line_no] = title_text
                        if "{{ Content }}" in template_split[line_no]:

                            content_text = template_split[line_no].replace("{{ Content }}", template_content.to_html())
                            template_split[line_no] = content_text
                        if 'href="/' in template_split[line_no] and '.css' not in template_split[line_no]:

                            content_text = template_split[line_no].replace('href="/', f'href="{base_path}')
                            template_split[line_no] = content_text
                    
                        if 'src="/' in template_split[line_no]:

                            content_text = template_split[line_no].replace('src="/', f'src="{base_path}')
                            template_split[line_no] = content_text
                    with open(os.path.join(dest_path,"index.html" ) , 'w') as html:
                        html.write("".join(template_split))
                                
            else:
                os.mkdir(os.path.join(dest_path, direc_or_file))
                generate_page_recursivly(os.path.join(from_path, direc_or_file), template_path=template_path, dest_path=os.path.join(dest_path, direc_or_file), direc_list=os.listdir(os.path.join(from_path, direc_or_file)),base_path=base_path)
    else:
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        else:
            dest_path = os.mkdir(os.getcwd(),"docs","contents")
        #dest_path = os.mkdir(os.path.join("public", "content"))       
        generate_page_recursivly(from_path=os.path.join(os.getcwd(), "content",),
                       template_path="src/template.html",
                       dest_path=dest_path ,
                         direc_list=os.listdir(os.path.join(os.getcwd(), "content",)),
                         base_path=base_path,
                         )
