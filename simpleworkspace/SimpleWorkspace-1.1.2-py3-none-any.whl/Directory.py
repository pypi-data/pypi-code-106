import hashlib
import os
from typing import Callable
import SimpleWorkspace as sw
import queue
import re

from SimpleWorkspace.File import Append


def Create(path: str):
    os.makedirs(path, exist_ok=True)


def ListFiles(searchDir: str, callback: Callable[[str], None] = None, includeDirs=True, includeFilter=None, satisfiedCondition: Callable[[str], bool] = None) -> (list[str] | None):
    """
    includeFilter:
        options takes a regex which searches full path of each file, if anyone matches a callback is called. Is not case sensitive
    satisfiedCondition:
        takes a callback that returns a bool, if it returns true, no more search is performed
    :returns
        if no callback is given, a list of all found filepaths will be returned\n
        otherwise None
    """

    if not os.path.exists(searchDir):
        return

    # only returned if callback was not given
    allEntries = [] if (callback is None) else None

    folders = queue.Queue()
    folders.put(searchDir)
    while folders.qsize() != 0:
        currentFolder = folders.get()
        try:
            currentFiles = os.listdir(currentFolder)
            for filePath in currentFiles:
                filePath = os.path.join(currentFolder, filePath)
                pathMatchesIncludeFilter = includeFilter == None or re.search(includeFilter, filePath, re.IGNORECASE)
                if os.path.isfile(filePath):
                    if pathMatchesIncludeFilter:
                        if callback != None:
                            callback(filePath)
                        else:
                            allEntries.append(filePath)
                    if satisfiedCondition != None and satisfiedCondition(filePath):
                        return
                else:
                    if includeDirs:
                        if pathMatchesIncludeFilter:
                            if callback != None:
                                callback(filePath)
                            else:
                                allEntries.append(filePath)
                        if satisfiedCondition != None and satisfiedCondition(filePath):
                            return
                    folders.put(filePath)
        except Exception as e:
            pass
    return allEntries
