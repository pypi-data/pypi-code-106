import os
import functools
import re

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
    
def StringToInteger(text:str, min=None, max=None, lessThan=None, moreThan=None) -> int | None:
    try:
        tmp = int(text)
        if(min != None):
            if(tmp<min):
                return None
        elif(moreThan != None):
            if(tmp <= moreThan):
                return None
        if(max != None):
            if(tmp > max):
                return None
        elif(lessThan != None):
            if(tmp >= lessThan):
                return None
        return tmp
    except Exception:
        return None

def Regex_Match(pattern:str, string:str):
    """
    finds all matches, default flags is case sensitive and multiline
    
    example:
        Regex_Match(r"/hej (.*?) /is", "hej v1.0 hej v2.2 hejsan v3.3") --> [['hej v1.0 ', 'v1.0'], ['hej v2.2 ', 'v2.2']]

    param pattern:
        use format "/regex/flags", allowed flags i=ignorecase, s=dotall
    
    returns:
        None if no matches found
    or
        2d list, where rows are matches, and each col corresponds to the capture groups
        example: [[match1, capture1, capture2][match2, capture1, capture2]]
    """   
    flagSplitterPos = pattern.rfind("/")
    if(pattern[0] != "/" and flagSplitterPos == -1):
        raise Exception("Pattern need to have format of '/pattern/flags'")
    regexPattern = pattern[1:flagSplitterPos] #remove first slash
    flags = pattern[flagSplitterPos+1:]
    flagLookup = {
        "i": re.IGNORECASE,
        "s": re.DOTALL,
        "m": re.MULTILINE
    }
    activeFlags = []
    for i in flags:
        activeFlags.append(flagLookup[i])
    
    if(re.DOTALL not in activeFlags and re.MULTILINE not in activeFlags):
        activeFlags.append(re.MULTILINE)

    flagParamValue = functools.reduce(lambda x, y: x | y, activeFlags)
    iterator = re.finditer(regexPattern, string, flags=flagParamValue)
    results = []
    for i in iterator:
        matches = []
        matches.append(i.group(0))
        if(len(i.groups()) > 0):
            matches = matches + list(i.groups())
        results.append(matches)
    if(len(results) == 0):
        return None
    return results

