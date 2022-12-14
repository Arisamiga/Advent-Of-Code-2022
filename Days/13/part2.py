
# Part 2 of Day 13


from functools import cmp_to_key


inputFile = open("./Days/13/input.txt", "r")

inputValues = inputFile.read().strip().replace("\n\n", "\n").split("\n")


def calulateValue(lists, list2):
    if isinstance(lists, list) and isinstance(list2, int):
        list2 = [list2]

    elif isinstance(lists, int) and isinstance(list2, list):
        lists = [lists]

    elif isinstance(lists, int) and isinstance(list2, int):
        if lists < list2:
            return True
        if lists == list2:
            return False
        return -1

    if isinstance(lists, list) and isinstance(list2, list):
        i = 0
        while i < len(lists) and i < len(list2):
            compare = calulateValue(lists[i], list2[i])
            if compare == True:
                return True
            if compare == -1:
                return -1
            
            i += 1

        if i == len(lists):
            if len(lists) == len(list2):
                return False
            return True
            
        return -1


lists = list(map(eval, inputValues))
lists.append([[2]])
lists.append([[6]])
lists = sorted(lists, key=cmp_to_key(calulateValue), reverse=True)

twoFound = 0
sixFound = 0
for index, List in enumerate(lists):
    if List == [[2]]:
        twoFound = index + 1
    elif List == [[6]]:
        sixFound = index + 1

print(twoFound * sixFound)