import AllInformation
import AllCommands

def ProgressDel(NOTEBOOK):
    while True:
        print(AllInformation.del_target_ask)
        deltarget=input()
        if deltarget==AllCommands.mode_stop_command:
            return
        else:
            deal_delete_word(NOTEBOOK,deltarget)
    return

def deal_delete_word(NOTEBOOK,deltarget):
    if deltarget in NOTEBOOK:
        print(deltarget+' '+NOTEBOOK[deltarget]+' '+AllInformation.del_found)
        delconfirm=input()
        if str(delconfirm) in AllCommands.del_confirm:
            del NOTEBOOK[deltarget]
            print(AllInformation.del_done)
        else:
            print(AllInformation.del_done_not)
    else:
        print(AllInformation.del_found_not)
    return