
# Part 1 of Day 11


inputFile = open("./Days/11/input.txt", "r")

inputValues = inputFile.read().strip().split("\n")

rounds = 20

Monkeys = []

for i in range(len(inputValues)):
    value = inputValues[i].replace(":", "")
    value = value.replace(",", "")
    split = value.split(" ")
    tempList = []
    if split[0] == "Monkey":
        numbers = inputValues[i + 1].replace("Starting items:", "").replace(" ", "").split(",")
        tempList.append([int(x) for x in numbers])
        tempList.append(inputValues[i + 2].split()[3:])
        tempList.append(inputValues[i + 3].split()[3:])
        tempList.append(inputValues[i + 4].split()[5:])
        tempList.append(inputValues[i + 5].split()[5:])
        Monkeys.append(tempList)

interacted = [0] * len(Monkeys)


def calculate(number, operation):
    lcal = number if operation[0] == 'old' else int(operation[0])
    rcal = number if operation[2] == 'old' else int(operation[2])
    if operation[1] == '+':
        return (lcal + rcal) // 3
    elif operation[1] == '*':
        return (lcal * rcal) // 3

for round in range(rounds):
    for index in range(len(Monkeys)):
        currentMonkey = Monkeys[index]
        for item in currentMonkey[0]:
            interacted[index] += 1
            value = calculate(item, currentMonkey[1])
            if value % int(currentMonkey[2][0]) == 0:
                Monkeys[int(currentMonkey[3][0])][0].append(value)
            else:
                Monkeys[int(currentMonkey[4][0])][0].append(value)
        currentMonkey[0].clear()

interacted = sorted(interacted, reverse=True)
print(interacted[0] * interacted[1])