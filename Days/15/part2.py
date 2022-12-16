
# Part 2 of Day 15

import re


inputFile = open("./Days/15/input.txt", "r")

inputValues = inputFile.read().split("\n")

yValue = 4000000

beaconPositions = []
sensorPositions = []

for line in inputValues:
    beacon = re.split('.+?(?=:)', line)[1]
    beacon = re.split("\W+", beacon)
    x,y = [int(s) for s in beacon if s.isdigit()]
    beaconPositions.append((x,y))

    sensor = line.split(":")[0]
    sensor = re.split("\W+", sensor)
    x,y = [int(s) for s in sensor if s.isdigit()]
    sensorPositions.append((x,y))


distances = []

for sensor in range(len(sensorPositions)):
    distances.append(abs(sensorPositions[sensor][0] - beaconPositions[sensor][0]) + abs(sensorPositions[sensor][1] - beaconPositions[sensor][1]))


positiveLines = []
negativeLines = []

for index,position in enumerate(sensorPositions):
    distance = distances[index]
    
    positiveLines.extend([position[0] - position[1] - distance, position[0] - position[1] + distance])
    negativeLines.extend([position[0] + position[1] - distance, position[0] + position[1] + distance])

positivePos = 0
negativePos = 0

for i in range(2 * len(sensorPositions)):
   for e in range(i + 1, (2 * len(sensorPositions))):
        # a and b are the x values of the two lines
        a,b = positiveLines[i], positiveLines[e]
        if abs(a-b) == 2:
            positivePos = min(a,b) + 1
        
        a,b = negativeLines[i], negativeLines[e]
        if abs(a-b) == 2:
            negativePos = min(a,b) + 1

x,y = (positivePos + negativePos) // 2, (negativePos - positivePos) // 2

answer = x * yValue + y

print(answer)

