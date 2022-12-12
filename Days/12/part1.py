
# Part 1 of Day 12


import heapq
import string

inputFile = open("./Days/12/input.txt", "r")

alphabet = list(string.ascii_lowercase)

startPosition = 0,0
EndPosition = 0,0

inputValues = inputFile.read().strip().split()

grid = [list(line) for line in inputValues]

direction = [[1,0],[-1,0],[0,1],[0,-1]]

gridLength = len(grid)
columnLength = len(grid[0])


for i in range(gridLength):
    for e in range(columnLength):
        character = grid[i][e]
        if character == "S":
            startPosition = i, e
        elif character == "E":
            EndPosition = i, e

def checkHeight(string):
    if string in alphabet:
        return alphabet.index(string)
    elif string == "S":
        return 0
    elif string == "E":
        return 25


def checkNear(x, y):
    for directionX,directionY in direction:
        xpos = x + directionX
        ypos = y + directionY
        if not (0 <= xpos < gridLength and 0 <= ypos < columnLength):
            continue

        if checkHeight(grid[xpos][ypos]) <= checkHeight(grid[x][y]) + 1 :
            # don’t want to store the entire sequence
            yield xpos,ypos


#  Using Dijksta's algorithm 

visitedCells = [[False] * columnLength for cell in range(gridLength)]

heap = [(0, startPosition[0], startPosition[1])]

while True:
    steps, x, y = heapq.heappop(heap)

    if visitedCells[x][y]:
        continue
    visitedCells[x][y] = True

    if (x, y) == EndPosition:
        print(steps)
        break

    for xpos,ypos in checkNear(x, y):
        heapq.heappush(heap, (steps + 1, xpos, ypos))