
# Part 1 of Day 8


inputFile = open("./Days/08/input.txt", "r")

inputValues = inputFile.read()

numberGrids = []
for line in inputValues.splitlines():
    numberGrids.append(list(map(int, line)))

answer = 0
for grid in range(len(numberGrids)):
    for num in range(len(numberGrids[grid])):
        currentNum = numberGrids[grid][num]
        if all(numberGrids[grid][newNum] < currentNum for newNum in range(num)) \
        or all(numberGrids[grid][newNum] < currentNum for newNum in range(num + 1, len(numberGrids[grid]))) \
        or all(numberGrids[newNum][num] < currentNum for newNum in range(grid)) \
        or all(numberGrids[newNum][num] < currentNum for newNum in range(grid + 1, len(numberGrids))):
            answer += 1

print(answer)
