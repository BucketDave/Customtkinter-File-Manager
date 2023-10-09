import os

c_dir = os.getcwd()

app_dir = os.path.join(c_dir, "Cisco_Syntax_FolderFiles")

def Boot():
    while not os.path.exists(app_dir):
        print("Cisco_Syntax_FolderFiles curently not found")
        
        os.makedirs(app_dir)
        if os.path.exists(app_dir):
            print(f"Created [Cisco_Syntax_FolderFiles] under parent [{app_dir}] successfully")

def Host_dir():
    return app_dir

def Find_Dir(name):
    print(f"find_dir {name}")
    dir_con = os.listdir(app_dir)

    for folder in dir_con:
        if name == folder:
            print(f"{name} in {app_dir} as {folder}")
            name_dir = os.path.join(app_dir, name)
            print(name_dir)
    return name_dir

def Find_File(folder_n, name):
    folder_n_path = Find_Dir(name=folder_n)
    print(f"folder_n_path = {folder_n_path}")
    if folder_n_path == None:
        return False
    else:
        for file in os.listdir(folder_n_path):
            if name == file:
                print(f"{name} == {file}")
                return os.path.join(folder_n_path, name)

def File_Contents(path):
    with open(path, 'r') as file_read:
        contents = file_read.read()
        return contents







Boot()

