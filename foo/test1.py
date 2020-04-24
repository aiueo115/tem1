import os
import json
import AllCommands
def input_list(name="source.json",location="..\\docs\\"):
    with open(location+name) as f:
        data=json.load(f)
    return data

a=input_list('source.json',"..\\docs\\")
print(a)
b=input()
print(b)

