
# Part 2 of Day 1

inputFile = open("./Days/01/input.txt", "r")

inputCalories = inputFile.read().split("\n")

currentHighest = 0

current = 0

totals = []

for i in inputCalories:
    if(i == ""):
        if(current > currentHighest):
            currentHighest = current
        totals.append(current)
        current = 0
    else:
        current += int(i)

totals.sort()
totals.reverse()

print(totals[0] + totals[1] + totals[2])