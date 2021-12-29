import os
import functools
import re

#these functions are directly implemented when imported

def LevelPrint(level, msg=None):
    for i in range(level):
        print("    ",end="", flush=True)
    if(msg != None):
        print(msg)

def LevelInput(level, msg=""):
    LevelPrint(level)
    return input(msg)

def AnyKeyDialog(msg=""):
    if(msg == ""):
        input("Press enter to continue...")
    else:
        input(msg+ " - Press enter to continue...")

def ClearConsoleWindow():
    os.system('cls' if os.name=='nt' else 'clear')
    return

def Print_SelectFileDialog(printlevel=1):
    LevelPrint(printlevel, "-Enter File Path:")
    FilePath = LevelInput(printlevel, "-")
    if os.path.exists(FilePath) == False:
        LevelPrint(printlevel+1, "-No such file found...")
        return None
    return FilePath
