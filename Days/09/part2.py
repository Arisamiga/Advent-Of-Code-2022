
# Part 2 of Day 9


inputFile = open("./Days/09/input.txt", "r")

inputValues = inputFile.read().split("\n")

knotParts = [[0,0] for i in range(10)]

def isTouching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


hasVisited = set()
hasVisited.add(tuple(knotParts[-1]))

for line in inputValues:
    split = line.split(" ")
    for times in range(int(split[1])):
        if split[0] == "L":
            knotParts[0][0] += -1
        elif split[0] == "R":
            knotParts[0][0] += 1
        elif split[0] == "U":
            knotParts[0][1] += 1
        elif split[0] == "D":
            knotParts[0][1] += -1
        for i in range(1, 10):
            hx,hy = knotParts[i - 1]
            tx,ty = knotParts[i]
            if not isTouching(hx, hy, tx, ty):
                sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                tx += int(sign_x)
                ty += int(sign_y)
            knotParts[i] = [tx, ty]
        # Note: This -1 Gets the last knotPart value if there not enough movement for all 10 knots then it will return [0,0]
        hasVisited.add(tuple(knotParts[-1]))

print(len(hasVisited))
