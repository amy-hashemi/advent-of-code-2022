import os
import csv

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day02_1")

with open("input.txt", "r") as file:
    data = csv.reader(file, delimiter = " ")
    games = [tuple(line) for line in data]

#initialization
score = 0

outcome = {"X": [('A', 'Z'), ('B', 'X'), ('C', 'Y')],
           "Y": [('A', 'X'), ('B', 'Y'), ('C', 'Z')], 
           "Z": [('A', 'Y'), ('B', 'Z'), ('C', 'X')]}

win_draw = {"X": 0, "Y": 3, "Z": 6}
responseVal = {"X": 1, "Y": 2, "Z": 3}

for round in games:
    score += win_draw[round[1]]
    for key, list in outcome.items():
        #check and see which outcome I need     
        if round[1] in key:
            for tup in list:
                #based on the outcome, check what the opponent played so I can determine what my response score is
                if round[0] == tup[0]:
                    score += responseVal[tup[1]]

print("Final Score:", score)





