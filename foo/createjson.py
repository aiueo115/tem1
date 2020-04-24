import json
import AllCommands
def CreateJson(name,location=AllCommands.source_location):
    with open(location+name,"w") as f:
        json.dump({},f)
    return