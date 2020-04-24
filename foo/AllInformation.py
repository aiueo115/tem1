import AllCommands
def ProgressOpenlist_introduction():
    print("press %s to open a notebook, %s to create a new notebook"\
        %(AllCommands.progress_list_open,AllCommands.progress_list_create))

passwd_wrong="wrong passwd"

mode_createlist_introduction="input the listname to create"
mode_createlist_wrong="oops! open it instead"
mode_createlist_done="create done"
mode_openlist_introduction="input the listname to open"
mode_openlist_wrong="oops! create it instead"
mode_openlist_done="open done"

def mode_select_introduction():
    print("%s for testmode; %s for addmode; %s for delmode; %s for showmode; %s for storemode; %s for delbookmode"\
        %(AllCommands.ModeTest,AllCommands.ModeAdd,AllCommands.ModeDel,AllCommands.ModeShow,AllCommands.ModeStore,AllCommands.ModeDelbook))
    print("press %s to quit"%(AllCommands.Progress_quit_command))
    return

mode_notice=" press "+AllCommands.mode_stop_command+" to exit"
mode_add_introduction="ModeAdd start"+mode_notice
mode_test_introduction="ModeTest start"+mode_notice
mode_del_introduction="ModeDel start"+mode_notice
mode_show_introduction="ModeShow start"+mode_notice
mode_store_done="successful stored"
mode_delbook_introduction="Delete the notebook? Please input the password"

test_order_select="select the order: "+\
AllCommands.test_order+" for order and "+AllCommands.test_random+" for random"
test_ctb_introduction="press %s to create ctb"%AllCommands.test_create_ctb
test_ctb_done="successful created"
test_ctb_done_not="fail to create"
add_que_ask="input the que"
add_ans_ask="input the ans"
add_confirm="press "+AllCommands.command_confirm_str+" to confirm"
add_done="successful add"
add_done_not="fail to add"
del_target_ask="input to delete"
del_done="successful delete"
del_done_not="fail to delete"
del_found="press "+AllCommands.command_confirm_str+" to confirm"
del_found_not="cannot find it"
delbook_done="successful delete"
delbook_done_not="fail to delete"