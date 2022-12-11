
# Part 1 of Day 10

inputFile = open("./Days/10/input.txt", "r")

inputValues = inputFile.read().split("\n")

x = 1

cyclesTotal = 0

sumMultipled = 0

targets = [20, 60, 100, 140, 180, 220]

def checkCyclesPoints(value):
    global cyclesTotal, x, sumMultipled
    if cyclesTotal in targets:
        print("Value at cycle | " + str(cyclesTotal) + ", x: " + str(x) + " | Multipled " + str(cyclesTotal) +  " * " + str(x) +  " = " + str(cyclesTotal * x) )
        sumMultipled += cyclesTotal * (x - value)

for line in inputValues:
    splitted = line.split(" ")

    if splitted[0] == "addx":
        x += int(splitted[1])
        cyclesTotal += 1
        checkCyclesPoints(int(splitted[1]))
        cyclesTotal += 1
        checkCyclesPoints(int(splitted[1]))
    elif splitted[0] == "noop":
        cyclesTotal += 1
        checkCyclesPoints(0)
print(sumMultipled)