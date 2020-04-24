from mode_test import ModeTest
from mode_add import ModeAdd
from mode_del import ModeDel
from mode_delbook import ModeDelbook
from mode_store import ModeStore
from mode_show import ModeShow
import AllCommands
import AllInformation
import data

def MainProgress():
    while True:
        AllInformation.mode_select_introduction()
        sel=input()
        if sel==AllCommands.Progress_quit_command:
            data.num_right=0
            data.num_wrong=0
            data.num_total=0
            data.NowBookName=""
            data.NowBook={}
            data.WrongList={}
            break
        elif sel==AllCommands.ModeTest:
            ModeTest(data.NowBook)
        elif sel==AllCommands.ModeAdd:
            ModeAdd(data.NowBook)
        elif sel==AllCommands.ModeDel:
            ModeDel(data.NowBook)
        elif sel==AllCommands.ModeShow:
            ModeShow(data.NowBook)
        elif sel==AllCommands.ModeStore:
            ModeStore(data.NowBookName,data.NowBook)
        elif sel==AllCommands.ModeDelbook:
            ModeDelbook(data.NowBookName)
            return
    return
