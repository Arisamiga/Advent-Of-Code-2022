


# Part 2 of Day 2


inputFile = open("./Days/02/input.txt", "r")

inputValues = inputFile.read().split("\n")

def getPoints(input):
    if(input == "Y"):
        return 2
    elif(input == "X"):
        return 1
    elif(input == "Z"):
        return 3
    else:
        return 0

def toWin(input):
    if(input == "C"):
        return "X"
    elif(input == "B"):
        return "Z"
    elif(input == "A"):
        return "Y"

def toLose(input):
    if(input == "C"):
        return "Y"
    elif(input == "B"):
        return "X"
    elif(input == "A"):
        return "Z"

def isTie(input):
    if(input == "C"):
        return "Z"
    elif(input == "B"):
        return "Y"
    elif(input == "A"):
        return "X"

totalWinnings = 0

for game in inputValues:
    valuesFormatted = game.split(" ")

    opponent = valuesFormatted[0]
    response = valuesFormatted[1]



    if (response == "Y"):
        response = isTie(opponent)
    elif (response == "X"):
        response = toLose(opponent)
    elif (response == "Z"):
        response = toWin(opponent)

    if(isTie(opponent) == response):
        # Draw
        totalWinnings += getPoints(response) + 3
    else:
        if(toWin(opponent) == response):
            # Best response to opponent
            totalWinnings += getPoints(response) + 6
        else:
            # Worst response to opponent
            totalWinnings += getPoints(response)
print(totalWinnings)

