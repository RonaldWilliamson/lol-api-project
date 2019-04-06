import requests
import json
import time
key="RGAPI-b5014d2d-5333-4a65-8c8c-c7e668c006ef"
# key1="RGAPI-dd9a4e6f-bd9c-47ad-9b37-074d88b5670c"
# key2="RGAPI-153cec9c-1ac1-4d9b-9d3d-a0ad1c33f2fb"
# key3="RGAPI-91eaac2d-e2d3-477c-85dc-21e0d05984b1"



keys=[key]
class lolapi():
    def __init__(self,key,start,count):
        self.count=0
        self.keys=key
        self.stoper=count
        self.stop=0
        self.z=[]
        self.bigD=[]
        self.bigZ=[]
        self.d=[start] 
        self.index=0
        self.sess=requests.Session()
        self.changeHead()
        self.crawl()
    def changeHead(self):
        if self.index%2 ==0:
            key=self.keys[0]
        else:
            key=self.keys[0]
        print(key)
        self.sess.headers.update({
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": key ,
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    })
    def matchhistory(self,x):
        x="https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+x
        print(x)
        time.sleep(2)
        return json.loads(self.sess.get(x).text)
    def getmatches(self,x):
        try:
            y=x['matches']
            for i in y:
                try:
                    self.z.append(i['gameId'])
                except:
                    print("wtf")
        except:
            print(x)
            
    def all_the_matches(self):
        print(len(self.d))
        x=0
        for i in self.d:
            x=x+1
            if x >=100:
                break
            print(i)
            self.bigD.append(i)
            if self.stop>=95:
                time.sleep(10)
                self.index+=1
                self.changeHead()
                self.stop=0
            self.getmatches(self.matchhistory(i))
            self.stop+=1
        self.d=[]
    def match(self,x):
        x="https://na1.api.riotgames.com/lol/match/v4/matches/"+str(x)
        time.sleep(2)

        j_son= json.loads(self.sess.get(x).text)
        # print(j_son)  
        try:
            work=j_son["participantIdentities"]
        
            for i in work:
                if i["player"]["accountId"] not in self.bigD:
                    self.d.append(i["player"]["accountId"])
            self.count+=1
            print(self.count)
            filename="data"+ str(self.count)+".json"

            with open(filename, 'w') as outfile:
                json.dump(j_son, outfile)

        except:
            print(x)
        
    def all_the_datas(self):
        print(len(self.z))
        x=0
        for i in self.z:
            x=x+1
            if x>=10000:
                break
            if self.stop>=95:
                time.sleep(10)
                self.stop=0
                self.index+=1
                self.changeHead()
            self.match(i)
            self.stop+=1
        self.z=[]

    def crawl(self):
        print("x")
        while len(self.d)!=0 or len(self.z) !=0:
            print("looped")

            dlist = open("dlist.txt",'w')
            zlist = open("zlist.txt",'w')
            for i in self.d:
                dlist.write(str(i)+"\n")
            for i in self.z:
                zlist.write(str(i))
            dlist.close()
            zlist.close()
                            
            if len(self.z) == 0:
                self.all_the_matches()
            else:
                self.all_the_datas()
            dlist = open("dlist.txt",'w')
            zlist = open("zlist.txt",'w')
            for i in self.d:
                dlist.write(str(i)+"\n")
            for i in self.z:
                zlist.write(str(i)+"\n")
x=lolapi(keys,"j38zVKEOG_Ihc508GqTT2ea-1dZXo_fnTX1qoD4BoAPJXQ",50000)

        




# req = requests.request('GET', 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/redkoolaid56')

# req = s.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/")
#2996557406/228022519
#firstDragon
# yMXR9Hs8ztFb3r8925g6-2dIrCjEckHTEOQb9jTyBsUaVA
# print(req.text)


