
# Part 1 of Day 9


inputFile = open("./Days/09/input.txt", "r")

inputValues = inputFile.read().split("\n")

hx, hy = 0, 0
tx, ty = 0, 0

def isTouching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


hasVisited = set()
hasVisited.add((tx, ty))

for line in inputValues:
    split = line.split(" ")
    for times in range(int(split[1])):
        if split[0] == "L":
            hx += -1
        elif split[0] == "R":
            hx += 1
        elif split[0] == "U":
            hy += 1
        elif split[0] == "D":
            hy += -1
        if not isTouching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += int(sign_x)
            ty += int(sign_y)
        
        hasVisited.add((tx, ty))

print(len(hasVisited))
