import os
import string

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day03")
data = open("input.txt", "r")

rucksackItems = []
priorityScore = 0
bagCount = 0
bagSet = [set() for i in range(3)]
print(bagSet)

#generate dicts that I'm going to be checking against
dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
dict_upper = dict.fromkeys(string.ascii_uppercase, 0)
dict_complete = {**dict_lower, **dict_upper}

print(dict_complete)

#build tuple of first and second item for each rucksack
for line in data:
    line = line.rstrip()
    bagSet[bagCount].add(line)
    print(bagSet[bagCount])
    bagCount += 1
    if bagCount == 3:
        result = bagSet[0].intersection(bagSet[1], bagSet[2])
        print(bagSet[0])
        bagCount = 0
        #print("found a common item! its: ", result)
        if result.islower():
            priority = int(format(ord(result))) - 96
            priorityScore += priority
        if result.isupper():
            priority = int(format(ord(result))) - 38
            priorityScore += priority
        bagSet.clear()
        break

print(priorityScore)