
# Part 1 of Day 15

import re


inputFile = open("./Days/15/input.txt", "r")

inputValues = inputFile.read().split("\n")

yValue = 2000000

beaconPositions = []
sensorPositions = []

for line in inputValues:
    beacon = re.split('.+?(?=:)', line)[1]
    beacon = re.split("[^\-\w]+", beacon)
    x,y = [int(s) for s in beacon if s[1:].isdigit()]
    beaconPositions.append((x,y))

    sensor = line.split(":")[0]
    sensor = re.split("[^\-\w]+", sensor)
    x,y = [int(s) for s in sensor if s[1:].isdigit()]
    sensorPositions.append((x,y))


distances = []

for sensor in range(len(sensorPositions)):
    distances.append(abs(sensorPositions[sensor][0] - beaconPositions[sensor][0]) + abs(sensorPositions[sensor][1] - beaconPositions[sensor][1]))


intervalList = []
for index,position in enumerate(sensorPositions):
    distanceX = distances[index] - abs(position[1] - yValue)

    if distanceX <= 0:
        continue
    intervalList.append((position[0] - distanceX, position[0] + distanceX))

allowedPositions = []
for x,y in beaconPositions:
    if y == yValue:
        allowedPositions.append(x)

answer = 0
for x in range(min([i[0] for i in intervalList]), max([i[1] for i in intervalList]) + 1):
    if x in allowedPositions:
        continue

    for left,right in intervalList:
        if left<= x <= right:
            answer += 1
            break
print(answer)