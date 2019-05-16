import json
import os
ids=[]
counter=0
cc=0
while True:
    counter+=1  
    filevar="solor"+str(counter)+".json"
    try:
        with open(filevar) as json_file:  
            data = json.load(json_file)

            
    except:
        print(filevar)
        cc+=1
        print(cc)
        continue
    if data['gameId'] not in ids:
        # print(filevar)
        ids.append(data['gameId'])
    else:
        
        os.remove(filevar)
    
    
