import os
import numpy as np
import pandas as pd
import csv

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day02_1")

with open("input.txt", "r") as file:
    data = csv.reader(file, delimiter = " ")
    games = [tuple(line) for line in data]

#initialization
score = 0
draw = 3
win = 6

responseVal = {"X": 1, "Y": 2, "Z": 3}
victoryScores = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
drawScores = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

for item in games:
    score += responseVal[item[1]]
    if item in victoryScores:
        score += win
    if item in drawScores:
        score += draw

print(score)
    





