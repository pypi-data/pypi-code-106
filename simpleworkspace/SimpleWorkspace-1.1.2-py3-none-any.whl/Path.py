import SimpleWorkspace as sw
import os

def FindEmptySpot(filepath: str):
    fileContainer = sw.File.FileContainer(filepath)
    TmpPath = fileContainer.tail + fileContainer.filename + fileContainer.fileEnding
    i = 1
    while os.path.exists(TmpPath) == True:
        TmpPath = fileContainer.tail + fileContainer.filename + "(" + str(i) + ")" + fileContainer.fileEnding
        i += 1
    return TmpPath