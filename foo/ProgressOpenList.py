import AllInformation
import AllCommands
import BookListUpdate
import list_input
import list_output
import data
from ProgressMain import MainProgress

def ProgressOpenlist(): 
    while True:
        BookListUpdate.BookListUpdate()
        AllInformation.ProgressOpenlist_introduction()
        waysel=input()
        if waysel==AllCommands.Software_quit_command:
            return
        if waysel==AllCommands.progress_list_create:
            mode_createlist()
        else:
            mode_openlist()
        MainProgress()
    return

def mode_createlist():
    print(AllInformation.mode_createlist_introduction)
    listname=input()
    if str(listname) in data.NOTEBOOKS or str(listname)+"json" in data.NOTEBOOKS:
        print(AllInformation.mode_createlist_wrong)
        deal_openlist(listname)
        print(AllInformation.mode_openlist_done)
    else:
        deal_createlist(listname)
        print(AllInformation.mode_createlist_done)
    return

def mode_openlist():
    print(AllInformation.mode_openlist_introduction)
    print(data.NOTEBOOKS)
    listname=input()
    if str(listname) not in data.NOTEBOOKS and str(listname)+".json" not in data.NOTEBOOKS:
        print(AllInformation.mode_openlist_wrong)
        deal_createlist(listname)
        print(AllInformation.mode_createlist_done)
    else:
        deal_openlist(listname)
        print(AllInformation.mode_openlist_done)
    return

def deal_createlist(listname):
    if listname[-5:]!=".json":
        listname=listname+".json"
    data.NowBook={} 
    data.NowBookName=listname
    list_output.output_list(data.NowBook,data.NowBookName)
    return

def deal_openlist(listname):
    if listname[-5:]!=".json":
        listname=listname+".json"
    data.NowBook=list_input.input_list(listname)
    data.NowBookName=listname
    return