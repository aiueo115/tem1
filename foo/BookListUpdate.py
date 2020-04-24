import os
import data
import AllCommands

def getlists(filedir):
    for files in os.walk(filedir):
        BookList=files[2]
    return BookList

def BookListUpdate():
    data.NOTEBOOKS=getlists(AllCommands.source_location)