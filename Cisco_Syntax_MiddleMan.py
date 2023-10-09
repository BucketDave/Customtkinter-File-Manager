import Cisco_Syntax_Backend

import os

def Host_dir_list():
    host_dir = Cisco_Syntax_Backend.Host_dir()
    host_dir_list = os.listdir(host_dir)
    return host_dir_list

def GetDir_List(path):
    list = os.listdir(path)
    print(list)
    return list

def MainButton_Dir(name):
    return_dir = Cisco_Syntax_Backend.Find_Dir(name)
    return return_dir

def SubButton_Contents(folder_n, name):
    verifyexist = Cisco_Syntax_Backend.Find_File(folder_n, name)
    print(f"verify {verifyexist}")
    if verifyexist:
        filecontents = Cisco_Syntax_Backend.File_Contents(verifyexist)
        if filecontents == None:
            pass
        else:
            return filecontents
    else:
        pass




