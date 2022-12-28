import os
import string

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day03")
data = open("input.txt", "r")

rucksackItems = []
priorityScore = 0
bagCount = 0
bagList = []

#generate dicts that I'm going to be checking against
dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
dict_upper = dict.fromkeys(string.ascii_uppercase, 0)
dict_complete = {**dict_lower, **dict_upper}
dict_complete_single_string = dict_complete

for line in data:
    line = line.rstrip()
    bagList.append(line)
    print(line)
    bagCount += 1

#every 3 items, we do our comparison and clear all data structures that were storing information from the previous triplet
    if bagCount == 3:
        for index in bagList:
            dict_complete_single_string = {x:0 for x in dict_complete}

            for letter in index:
                print(letter)
                print(dict_complete[letter])              
                if dict_complete_single_string[letter] == 0:
                    if dict_complete[letter] < 3:
                        dict_complete[letter] = dict_complete[letter] + 1

                dict_complete_single_string[letter] = dict_complete_single_string[letter] + 1

        for item in dict_complete:
            if dict_complete[item] == 3:
                if item.islower():
                    priority = int(format(ord(item))) - 96
                    priorityScore += priority
                if item.isupper():
                    priority = int(format(ord(item))) - 38
                    priorityScore += priority
                break
        
        dict_complete = {x:0 for x in dict_complete}
        bagCount = 0
        bagList.clear()

print(priorityScore)