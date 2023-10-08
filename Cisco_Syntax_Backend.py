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
    dir_con = os.listdir(app_dir)

    for folder in dir_con:
        if name == folder:
            print(f"{name} in {app_dir} as {folder}")
            name_dir = os.path.join(app_dir, name)
            print(name_dir)
            return name_dir
    else:
        return False

Boot()

