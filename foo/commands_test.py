import json
import random
import AllInformation
import list_output
import AllCommands
import data
def ProgressTest(NOTEBOOK):
    for (i,j) in NOTEBOOK.items():
        ans=deal_test_word(i,j)
        if ans==AllCommands.mode_stop_command:
            break
    return    

def ProgressTestRandom(NOTEBOOK):
    keys=[]
    for i in NOTEBOOK.keys():
        keys.append(i)
    randomkeys=random.sample(keys,len(keys))
    for j in randomkeys:
        ans=deal_test_word(j,NOTEBOOK[j])
        if ans==AllCommands.mode_stop_command:
            break
    return
    


def deal_test_word(que,ans):
    print("tell me what is "+que+"?")
    ans_given=input()
    if ans_given==ans:
        TestRight()
    elif ans_given==AllCommands.test_jump:
        TestJump()
    elif ans_given==AllCommands.mode_stop_command:
        return ans_given
    else:
        TestWrong(que,ans)
    return ans_given

def TestRight():
    print("Great!")
    data.num_right+=1
    data.num_total+=1
    return

def TestWrong(que,ans):
    print("Wrong!")
    data.num_wrong+=1
    data.num_total+=1
    print("it is "+ans)
    data.CtbBook[que]=ans
    return

def TestJump():
    print("jump!")

def TestConclude():
    print("total: "+str(data.num_total))
    print("right: "+str(data.num_right))
    print("wrong: "+str(data.num_wrong))


def deal_ctb():
    print(AllInformation.test_ctb_introduction)
    ctbsel=input()
    if ctbsel==AllCommands.test_create_ctb:
        create_ctb()
        print(AllInformation.test_ctb_done)
    else:
        print(AllInformation.test_ctb_done_not)
    clean_ctb()
    return
        

def create_ctb():
    list_output.output_list(data.CtbBook,data.NowBookName[:-5]+"_ctb.json")
    return

def clean_ctb():
    data.num_right=0
    data.num_total=0
    data.num_wrong=0
    data.CtbBook={}
    return