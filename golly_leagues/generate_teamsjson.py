import uuid
import random
import json

colors = [
    "#a0e7e5",
    "#ff66cc",
    "#9963ab",
    "#e7d7c1",
    "#ffb627",
    "#697a21",
    "#0dab76",
    "#ff1717",
    "#3e92cc",
    "#f2c57c",
    "#e86215",
    "#a0e7e5",
    "#53917e",
    "#ef6f6c",
    "#f08700",
    "#990000"
]
colors.sort()

with open('city_names.txt', 'r') as f:
    cities = f.readlines()
cities = [line.strip() for line in cities]

with open('team_nick_names.txt', 'r') as f:
    nicknames = f.readlines()
nicknames = [line.strip() for line in nicknames]

leagues = ['Hot League', 'Cold League']
divisions = ['Fire Division', 'Water Division']
teams_per_div = 4

if len(leagues)*len(divisions)*teams_per_div > len(colors):
    raise Exception("Error: need more colors!")

teams = []

iC = 0
for iL, league in enumerate(leagues):
    for iD, division in enumerate(divisions):
        for iT in range(teams_per_div):
            team = {}
            city = random.choice(cities)
            nick = random.choice(nicknames)
            team['teamName'] = f"{city} {nick}" 
            team['teamAbbr'] = "".join([z[0] for z in team['teamName'].upper().split(" ")]) 
            team['teamColor'] = colors[iC]
            team['teamId'] = str(uuid.uuid4())
            team['league'] = league
            team['division'] = division
            teams.append(team)

with open('teams.json', 'w') as f:
    json.dump(teams, f, indent=4)

