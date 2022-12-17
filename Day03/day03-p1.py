import os
import string

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day03")
data = open("input.txt", "r")

rucksackItems = []
priorityScore = 0
itemCount = 0

#generate dicts that I'm going to be checking against
dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
dict_upper = dict.fromkeys(string.ascii_uppercase, 0)
dict_complete = {**dict_lower, **dict_upper}

print(dict_complete)

#build tuple of first and second item for each rucksack
for line in data:
    doubleItem = line.rstrip()
    firstItem = doubleItem[:len(doubleItem)//2]
    secondItem = doubleItem[len(doubleItem)//2:]
    rucksackPair = (firstItem, secondItem)
    rucksackItems.append(rucksackPair)

for collection1, collection2 in rucksackItems:
    dict_complete = {x:0 for x in dict_complete}
    for item1 in collection1:
        if dict_complete[item1] == 0:
            dict_complete[item1] = 1
    for item2 in collection2:
        if dict_complete[item2] == 1:
            print("found a duplicate character between the two collections! The character is: ", item2)
            if item2.islower():
                priority = int(format(ord(item2))) - 96
                priorityScore += priority
            if item2.isupper():
                priority = int(format(ord(item2))) - 38
                priorityScore += priority
            break

print(priorityScore)