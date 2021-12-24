from station import Station
from metro import Metro
from agent import Agent
import numpy as np
import time
import json
 
# Opening JSON file
f = open('plan.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

stationsLines = {}

numberOfLines = data["numberOfLines"]
metros = []


# Generate random world from file

# Intiate the dictionary of lines
for line in range(numberOfLines):
    stationsLines[line] = []

for station in np.random.permutation(data["stations"]):
    # Each station is randomly added to multiple lines

    # For each line, say 1 if selected, 0 otherwise
    metroRandomLineChoice = np.random.choice([0, 1], size=(numberOfLines,))

    for idx,line in enumerate(metroRandomLineChoice):
        if line == 1:
            stationsLines[idx].append(Station("station{}".format(station)))

for line in range(numberOfLines):
    #Create connection of stations on the same line
    stationsOfLine = stationsLines[line]

    if len(stationsOfLine) > 0:
        for idx in range(len(stationsOfLine)):
            if idx==0:
                stationsOfLine[idx].defineNext(stationsOfLine[idx+1],line)
            elif idx==len(stationsOfLine)-1:
                stationsOfLine[idx].definePrevious(stationsOfLine[idx-1],line)
            else:
                stationsOfLine[idx].defineNext(stationsOfLine[idx+1],line)
                stationsOfLine[idx].definePrevious(stationsOfLine[idx-1],line)

        metro = Metro(line,stationsOfLine[0])
        metros.append(metro)

if __name__ == '__main__':

    while True:        
        time.sleep(1)
        print("Leaving {}...".format(metros[0].position.name))
     
        time.sleep(1)
        metros[0].goToNext()
        print("...Arrived to {} !".format(metros[0].position.name))