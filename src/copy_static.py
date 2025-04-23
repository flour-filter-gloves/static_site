import os
import shutil

def copy_static(dest=os.path.join(os.getcwd()) ,src=None, direc_list = None):
    if direc_list:
        for item in direc_list:
            if os.path.isfile(os.path.join(src,item)):
                shutil.copy(os.path.join(src,item) ,os.path.join(dest, item) ) 

            else:

                os.mkdir(os.path.join(dest,item))
                copy_static(os.path.join(dest,item),os.path.join(src,item), os.listdir(os.path.join(src,item)))                
    else:
        if os.path.exists(os.path.join(dest,"docs")):
                shutil.rmtree(os.path.join(dest,"docs"))
                os.mkdir(os.path.join(dest,"docs"))
        else:
             os.mkdir(os.path.join(dest,"docs"))
        copy_static(dest=os.path.join(os.getcwd(), "docs"),src=os.path.join(os.getcwd(),"static"),direc_list=os.listdir(os.path.join(os.getcwd(),"static")))

