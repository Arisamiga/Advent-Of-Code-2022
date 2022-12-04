
# Part 2 of Day 4


inputFile = open("./Days/04/input.txt", "r")

inputValues = inputFile.read().split("\n")

duplicateSum = 0


for pair in inputValues:
    firstPair = pair.split(",")[0].split("-")
    secondPair = pair.split(",")[1].split("-")
    for section in range(int(firstPair[0]) + 1, int(firstPair[1])):
        firstPair.append(str(section))
    for section in range(int(secondPair[0]) + 1, int(secondPair[1])):
        secondPair.append(str(section))

    firstPair = [int(x) for x in firstPair]
    secondPair = [int(x) for x in secondPair]
    firstPair.sort()
    secondPair.sort()
    firstPair = list(dict.fromkeys(firstPair))
    secondPair = list(dict.fromkeys(secondPair))
    combied = firstPair + secondPair
    
    if set(firstPair).issuperset(set(secondPair)):
        duplicateSum += 1
    elif set(secondPair).issuperset(set(firstPair)):
        duplicateSum += 1
    elif len(combied) != len(set(combied)):
        duplicateSum += 1

print(duplicateSum)