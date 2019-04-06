import json
red =0
blue=0

counter=0
while True:
    filevar="solor"+counter+".json"
    counter+=1
    try:
        with open(filevar) as json_file: 
            data = json.load(json_file)
    except:
        continue
    if data['team'][0]['win'] =='Fail':
        red+=1
    else :
        blue+=1
print(blue/red)

