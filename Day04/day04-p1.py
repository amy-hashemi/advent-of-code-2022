import os
import string
import csv

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day04")

def extract_range(first, second, containedCount):

    firstRange = [eval(item) for item in first]
    secondRange = [eval(item) for item in second]

    print(firstRange)
    print(secondRange)

    if (firstRange[0] >= secondRange[0] and firstRange[1] <= secondRange[1]) or (secondRange[0] >= firstRange[0] and secondRange[1] <= firstRange[1]):
        print("found a fully encapsulated range")
        containedCount += 1
    else:
        print("not a fully encapsulated range")

    return containedCount

def main():
    containedCount = 0
    with open("input.txt", "r") as f:
        for row in csv.reader(f, delimiter = ","):
            firstRange = row[0].split("-")
            secondRange = row[1].split("-")
            containedCount = extract_range(firstRange, secondRange, containedCount)
            print(containedCount)


if __name__ == "__main__":
    main()
        
        







    
