
# Part 2 of Day 7


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
            elif not line.isalpha():
                dir_name = line.split(" ")[1]
                fileChildren[fullPath].append(f"{fullPath}/{dir_name}")
        dirSizes[fullPath] = sizesSum

def deepSearch(Path):
    size = dirSizes[Path]
    for child in fileChildren[Path]:
        size += deepSearch(child)
    return size


currentSpace = 70000000 - deepSearch("/") # Use root directory size to calculate the space left
requiredSpace = 30000000 - currentSpace # Use the currentspace to calculate the space needed

answer = 30000000 # Set the answer to the maximum possible value
for currentPath in dirSizes:
    pathSize = deepSearch(currentPath)
    if pathSize >= requiredSpace:
        answer = min(answer, pathSize)

print(answer)