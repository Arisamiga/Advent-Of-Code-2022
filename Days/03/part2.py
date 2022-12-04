

# Part 2 of Day 3

import string

inputFile = open("./Days/03/input.txt", "r")

inputValues = inputFile.read().split("\n")

alphabet = list(string.ascii_lowercase)

upperAlphabet = list(string.ascii_uppercase)

rucksackSum = 0

line = 0

itemList = []

for items in inputValues:
    if(items != "" and line == 2):
        line = 0
        itemList.append(items)
        for letter in itemList[0]:
            if(letter in itemList[1] and letter in itemList[2]):
                if(letter not in alphabet):
                    rucksackSum += upperAlphabet.index(letter) + 27
                    break
                else:
                    rucksackSum += alphabet.index(letter) + 1
                    break
        itemList = []
    else:
        itemList.append(items)
        line += 1

print(rucksackSum)