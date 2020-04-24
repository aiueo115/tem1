import json
import AllCommands
def output_list(list_output,name='target.json',location="..\\docs\\"):
    with open(location+name,'w') as writefile:
        json.dump(list_output,writefile)
    return