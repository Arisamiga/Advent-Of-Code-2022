
# Part 1 of Day 14


inputFile = open("./Days/14/input.txt", "r")

inputValues = inputFile.read().split("\n")

sandSource = 500,0


alreadyFilled = set()

for line in inputValues:
    coordinates = []
    for string in line.split(" -> "):
        x, y = map(int, string.split(","))
        coordinates.append([x, y])

    for i in range(1, len(coordinates)):
        currentX, currentY = coordinates[i]
        previousX, previousY = coordinates[i - 1]

        if currentY != previousY:
            for y in range(min(currentY, previousY), max(currentY, previousY) + 1):
                alreadyFilled.add((currentX, y))

        if currentX != previousX:
            for x in range(min(currentX, previousX), max(currentX, previousX) + 1):
                alreadyFilled.add((x, currentY))
                
maximumY = max([coordinates[1] for coordinates in alreadyFilled])

def sandFalling():
    x,y = sandSource

    while y <= maximumY:
        if (x,y + 1) not in alreadyFilled:
            y += 1
            continue
        if (x - 1, y + 1) not in alreadyFilled:
            x -= 1
            y += 1
            continue
        if (x + 1, y + 1) not in alreadyFilled:
            x += 1
            y += 1
            continue

        alreadyFilled.add((x,y))
        return True
    return False

answer = 0

while True:
    fallSand = sandFalling()

    if fallSand == False:
        break

    answer += 1

print(answer)