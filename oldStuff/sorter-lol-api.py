import json 
import os
counter=0
countersgame=45000
while True:
    counter+=1  
    filevar="data"+str(counter)+".json"
    try:
        with open(filevar) as json_file:  
            data = json.load(json_file)
            os.remove(filevar)
    except:
        continue
    try:
        
        if data["gameMode"]=="CLASSIC" and data["queueId"]==420:
            filename="solor"+ str(countersgame)+".json"

            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
            countersgame+=1
            
    except:
        continue
