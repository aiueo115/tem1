import AllInformation
import AllCommands

def ProgressAdd(NOTEBOOK):
    while True:
        print(AllInformation.add_que_ask)
        Add=input()
        if Add==AllCommands.mode_stop_command:
            return
        else:
            que=Add
        print(AllInformation.add_ans_ask)
        Add=input()
        if Add==AllCommands.mode_stop_command:
            return
        else:
            ans=Add 
        deal_add_word(que,ans,NOTEBOOK)
    return



def deal_add_word(que,ans,NOTEBOOK):
    print(que+" "+ans+" "+AllInformation.add_confirm)
    addconfirm=input()
    if str(addconfirm) in AllCommands.add_confirm:
        NOTEBOOK[que]=ans
        print(AllInformation.add_done)
    else:
        print(AllInformation.add_done_not)
    return