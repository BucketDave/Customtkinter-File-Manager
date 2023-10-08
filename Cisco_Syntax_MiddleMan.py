import Cisco_Syntax_Backend

import os

def Host_dir_list():
    host_dir = Cisco_Syntax_Backend.Host_dir()
    host_dir_list = os.listdir(host_dir)
    return host_dir_list

def MainButton_Dir(name):
    return_dir = Cisco_Syntax_Backend.Find_Dir(name)
    return return_dir

def GetDir_List(path):
    list = os.listdir(path)
    print(list)
    return list

