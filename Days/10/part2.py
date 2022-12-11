
# Part 2 of Day 10

inputFile = open("./Days/10/input.txt", "r")

inputValues = inputFile.read().split("\n")

x = 1

cyclesTotal = 0

targets = [20, 60, 100, 140, 180, 220]

xList = [1] * 241

for line in inputValues:
    splitted = line.split(" ")

    if splitted[0] == "addx":
        xList[cyclesTotal + 1] = x
        x += int(splitted[1])
        cyclesTotal += 2
        xList[cyclesTotal] = x
    elif splitted[0] == "noop":
        cyclesTotal += 1
        xList[cyclesTotal] = x

answer = [[None] * 40 for empty in range(6)]

for row in range(6):
    for col in range(40):
        place = row * 40 + col + 1
        if abs(xList[place - 1] - (col)) <= 1:
            answer[row][col] = "##"
        else:
            answer[row][col] = "  "

for Rows in answer:
    print("".join(Rows))