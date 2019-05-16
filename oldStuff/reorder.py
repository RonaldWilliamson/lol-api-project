import json
import os
counter=30000
cc=30000
while True:
    counter+=1  
    filevar="solor"+str(counter)+".json"
    filename="solor"+str(cc)+".json"
    try:
        with open(filevar) as json_file:  
            data = json.load(json_file)
            cc+=1
        print(filevar,filename)
        os.remove(filevar)
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
    except:
        continue
