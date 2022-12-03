

# Part 1 of Day 3

import string

inputFile = open("input.txt", "r")

inputValues = inputFile.read().split("\n")

alphabet = list(string.ascii_lowercase)

upperAlphabet = list(string.ascii_uppercase)

rucksackSum = 0

for items in inputValues:
    if(items != ""):
        firstContainer = slice(0, len(items)//2)
        secondContainer = slice(len(items)//2, len(items))
        for letter in list(items[firstContainer]):
            if(letter in items[secondContainer]):
                if(letter not in alphabet):
                    rucksackSum += upperAlphabet.index(letter) + 27
                    break
                else:
                    rucksackSum += alphabet.index(letter) + 1
                    break

print(rucksackSum)