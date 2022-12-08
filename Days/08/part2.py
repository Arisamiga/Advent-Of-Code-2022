
# Part 2 of Day 8


inputFile = open("./Days/08/input.txt", "r")

inputValues = inputFile.read()

numberGrids = []
for line in inputValues.splitlines():
    numberGrids.append(list(map(int, line)))

answer = 0
for grid in range(len(numberGrids)):
    for num in range(len(numberGrids[grid])):
        currentNum = numberGrids[grid][num]
        Up = 0
        Down = 0
        Left = 0
        Right = 0
        for left in range(num -1, -1, -1):
            Left += 1
            if numberGrids[grid][left] >= currentNum:
                break
        for right in range(num + 1, len(numberGrids[grid])):
            Right += 1
            if numberGrids[grid][right] >= currentNum:
                break
        for up in range(grid - 1, -1, -1):
            Up += 1
            if numberGrids[up][num] >= currentNum:
                break
        for down in range(grid + 1, len(numberGrids)):
            Down += 1
            if numberGrids[down][num] >= currentNum:
                break
        answer = max(answer, Up * Down * Left * Right)
print(answer)