
# Part 1 of Day 5

lines = []

with open("./Days/05/input.txt") as f:
    for line in f.readlines():
        lines.append(line)
movements = []
movementsStart = False
stacks = []

for Crates in lines:
    if not Crates.replace(" ", "").strip():
        movementsStart = True
        continue
    if not movementsStart:
        stacks.append(Crates)
    else:
        movements.append(Crates)
colums = [[line[x] for line in stacks] for x in range(len(stacks[0]))]
formatedColums = []
for i in colums:
    if i[-1].strip():
        i = [x for x in i if x.strip()]
        i.reverse()
        i.pop(0)
        formatedColums.append(i)

for Move in movements:
    moveNums = [int(i) for i in Move.split() if i.isdigit()]
    numToMove = moveNums[0]
    numMoveFrom = moveNums[1]
    numMoveTo = moveNums[2]
    for i in range(int(numToMove)):
        formatedColums[int(numMoveTo) - 1].append(formatedColums[int(numMoveFrom) - 1].pop())
print("".join([x[-1] for x in formatedColums]))