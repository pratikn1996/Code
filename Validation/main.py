import json

jsonfile=open('Team.json','r')
jsondata=jsonfile.read()
data=json.loads(jsondata)
playingelv=data['player']
Outsiders="India"
print("The players from foreign countries are")
for i in range(len(playingelv)):
    if playingelv[i].get("country") != Outsiders:
      playername = []
      playername.append(playingelv[i].get("name"))
      print(playername)

Skill="Wicket-keeper"
for j in range(len(playingelv)):
    if playingelv[j].get("role") == Skill:
        print("the wicket-keeper is " + playingelv[i].get("name"))