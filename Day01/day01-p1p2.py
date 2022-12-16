import os
import heapq

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day01_1-2")
files = os.listdir(cwd)
print("files in cwd: %s" % files)

# import input file & read contents
file1 = open("input.txt", "r")
caloriesRead = file1.readlines()

elfCalorieSum = 0
calorieInt = 0
caloriesList = []
maxElvesHeap = [0,0,0]
heapq.heapify(maxElvesHeap)

for item in caloriesRead:
    if item != "\n":
        calorieInt = int(item)
        print("calorieInt: ", calorieInt)
        elfCalorieSum = elfCalorieSum + calorieInt
    
    if item == "\n":
        print("elfCalorieSum: ", elfCalorieSum)
        caloriesList.append(elfCalorieSum)
        elfCalorieSum = 0
        heapq.heappushpop(maxElvesHeap, elfCalorieSum)

caloriesList.sort(reverse=True)
print(caloriesList)

print("The most calories carried by an elf is: %d" % (caloriesList[0]))

for item in caloriesList:
    if item:
        if item > maxElvesHeap[0]:
            heapq.heapreplace(maxElvesHeap, item)

print(maxElvesHeap)
print(sum(maxElvesHeap))
        

    
        


