
# Part 1 of Day 13


inputFile = open("./Days/13/input.txt", "r")

inputValues = inputFile.read().strip().split("\n\n")


def calulateValue(lists, list2):
    if isinstance(lists, list) and isinstance(list2, int):
        list2 = [list2]
    if isinstance(lists, int) and isinstance(list2, list):
        lists = [lists]
    if isinstance(lists, int) and isinstance(list2, int):
        if lists < list2:
            return True
        if lists == list2:
            return False
        return None
    if isinstance(lists, list) and isinstance(list2, list):
        i = 0
        while i < len(lists) and i < len(list2):
            compare = calulateValue(lists[i], list2[i])
            if compare == True:
                return True
            if compare == None:
                return None
            
            i += 1

        if i == len(lists):
            if len(lists) == len(list2):
                return False
            return True

            
        return None


answer = 0

for index, content in enumerate(inputValues):
    lists,list2 = map(eval, content.split("\n"))
    if calulateValue(lists, list2) == True:
        answer += index + 1

print(answer)