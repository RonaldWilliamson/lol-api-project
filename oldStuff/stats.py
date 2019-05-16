import json
counter=0
while True:
    counter+=1  
    filevar="solor"+str(counter)+".json"
    try:
        with open(filevar) as json_file:  
            data = json.load(json_file)
        
