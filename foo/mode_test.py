import commands_test
import AllCommands
from list_output import output_list
import AllInformation 
import data
def ModeTest(NOTEBOOK):
    print( AllInformation.mode_test_introduction)
    print(AllInformation.test_order_select)
    orderselect=input()
    if orderselect==AllCommands.test_order:
        commands_test.ProgressTest(NOTEBOOK)
    else:
        commands_test.ProgressTestRandom(NOTEBOOK)
    commands_test.TestConclude()
    commands_test.deal_ctb()
    return
