
# Part 1 of Day 1

inputFile = open("input.txt", "r")

inputCalories = inputFile.read().split("\n")

currentHighest = 0

current = 0

for i in inputCalories:
    if(i == ""):
        if(current > currentHighest):
            currentHighest = current
        current = 0
    else:
        current += int(i)
    
print(currentHighest)