import os
import AllInformation
import AllCommands

def ModeDelbook(bookname):
    print(AllInformation.mode_delbook_introduction)
    passwd=input()
    if passwd==AllCommands.password:
        os.remove(AllCommands.source_location+bookname)
        print(AllInformation.delbook_done)
    else:
        print(AllInformation.passwd_wrong)
        print(AllInformation.delbook_done_not)