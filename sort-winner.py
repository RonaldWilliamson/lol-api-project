import json 
    
    
    
    
filevar="data"+str(counter)+".json"
try:
    with open(filevar) as json_file:  
        data = json.load(json_file)