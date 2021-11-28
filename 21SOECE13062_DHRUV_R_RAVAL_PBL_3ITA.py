import os
import os.path
import shutil
extension=['.py','.txt','.jpeg','.zip','.php','.html','.c','.c++','.doc','.pdf','.png','.mp4']
file_name_list  = ['Python','Text Files','Images','ZIP','PHP files','HTML files','C Files','C++ Files','Doc files','PDF files','Images','Videos']

x=0
while x !=1:
    origin_input = input("Enter Origin Path :- ")
    try:
        os.chdir(origin_input)
        x=1
    except:
        x=0
        print("Invalid input path ")

path = os.listdir()
x=0
while x!=1:
    destination_input = input("Destination path :- ")
    try:
        os.chdir(destination_input)
        x=1
    except:
        x=0
        print("Invalid Destination path")
for i in path:
    skip = 0
    try:
        slice_var=i.index('.')
    except:
        skip = 1
    if skip ==0:
        extracted_extension = i[slice_var:]
    
        if extracted_extension in extension:
            pos=extension.index(extracted_extension)
            folder_name = file_name_list[pos]
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
            try:
                shutil.move(f"{origin_input}/{i}",f'/{folder_name}')
            except:
                print(f"{i} is already exists on {folder_name}")
