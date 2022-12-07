
# Part 1 of Day 7


from collections import defaultdict


inputFile = open("./Days/07/input.txt", "r")

inputValues = ("\n" + inputFile.read().strip()).split("\n$ ")[1:]

Paths = []
dirSizes = defaultdict(int)
fileChildren = defaultdict(list)

for line in inputValues:
    lines = line.split("\n")
    commandInputs = lines[0]
    commandOutputs = lines[1:]
    commandParts = commandInputs.split(" ")

    if commandParts[0] == "cd":
        if commandParts[1] == "..":
            Paths.pop()
        else:
            Paths.append(commandParts[1])
    elif commandParts[0] == "ls":
        fullPath = "/".join(Paths)

        sizesSum = 0
        for line in commandOutputs:
            if not line.startswith("dir"):
                sizesSum += int(line.split(" ")[0])
            else:
                dir_name = line.split(" ")[1]
                fileChildren[fullPath].append(f"{fullPath}/{dir_name}")
        dirSizes[fullPath] = sizesSum

def deepSearch(Path):
    size = dirSizes[Path]
    for child in fileChildren[Path]:
        size += deepSearch(child)
    return size

answer = 0
for currentPath in dirSizes:
    if deepSearch(currentPath) <= 100000:
        answer += deepSearch(currentPath)

print(answer)