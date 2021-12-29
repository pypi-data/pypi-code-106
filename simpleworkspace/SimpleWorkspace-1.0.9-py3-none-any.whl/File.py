import hashlib
import os
from typing import Callable
import SimpleWorkspace as sw
import queue
import re


class FileInfo:
    """
    example case: a/b/test.exe\n
    - filename      = test\n
    - fileExtension = .exe\n
    - tail          = a/b/\n
    - head          = test.exe\n
    - rawPath       = a/b/test.exe\n

    - If no match can be found for any property, they will default to empty string
    """

    tail = ""
    head = ""
    filename = ""
    fileExtension = ""
    rawPath = ""

    def __init__(self, filepath) -> None:
        self.rawPath = filepath
        headTail = os.path.split(filepath)
        self.tail = headTail[0]
        if self.tail != "":
            self.tail += "/"
        self.head = headTail[1]
        baseName = headTail[1]

        fullFilename = baseName.rsplit(".", 1)
        self.filename = fullFilename[0]
        if len(fullFilename) == 2:
            self.fileExtension = "." + fullFilename[1]




def SHA256(filePath):
    sha256 = hashlib.sha256()
    Read(filePath, lambda x: sha256.update(x), readSize=sw.Conversion.Bytes.MB * 1, getBytes=True)
    return sha256.hexdigest()


def Read(filePath: str, callback: Callable[[str], None] = None, readSize=-1, readLimit=-1, getBytes=True):
    """
    :(opt) callback: call a lambda function each time a file is read with the readSize\n
    - if no callback is used, a return value with file content will be returned\n
    :(opt) readSize: amount of bytes to read at each callback, default of -1 reads all at once\n
    :(opt) ReadLimit: Max amount of bytes to read, default -1 reads until end of file\n
    :(opt) getBytes: default True, specifies if the return data is in string or bytes format\n
    """

    content = b""
    openMode = "rb"
    if getBytes == False:
        openMode = "r"
        content = ""

    if (readSize == -1 and readLimit >= 0) or (readLimit < readSize and readLimit >= 0):
        readSize = readLimit
    totalRead = 0
    with open(filePath, openMode) as file:
        while True:
            if readLimit != -1 and totalRead >= readLimit:
                break
            data = file.read(readSize)
            totalRead += readSize
            if data:
                if callback == None:
                    content += data
                else:
                    callback(data)
            else:
                break
    return content

def Create(filepath: str, data=None):
    openMode = "wb"
    if type(data) is str:
        openMode = "w"
    with open(filepath, openMode) as file:
        if data is not None:
            file.write(data)


def Append(filepath:str, data: bytes | str):
    openMode = None
    if type(data) is bytes:
        openMode = "ab"
    elif type(data) is str:
        openMode = "a"
    else:
        raise Exception("Bytes or string can be used to append to file")
    with open(filepath, openMode) as file:
        file.write(data)



