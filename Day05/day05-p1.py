import os
import re
import queue
import collections

cwd = os.chdir("c:\\Users\\AmyHashemi\\Python\\advent-of-code-2022\\Day05")

def generate_stacks() -> queue:
    bins = [item for item in range(1,10)]
    starts = [item for item in range(0,36,4)]
    myKey = {}
    myQueues = [queue.Queue() for item in range(1,10)]

    for key in starts:
        for value in bins:
            myKey[key] = value
            bins.remove(value)
            break

    with open("LIFOQueueInput.txt", "r") as f:
        for line in f:
            crates = list(re.finditer(r"\[(\w)\]", line))
            for crate in crates:
                cratePosition = myKey[crate.start()]
                print(cratePosition)
                myQueues[myKey[crate.start()]-1].put(crate)

    print("Top of my stacks: ")
    for item in myQueues:
        print(item.get())
        
    return myQueues

def move_crates(moves: list, myQueues: list) -> queue:
    print(moves)
    i = 0
    if i < moves[0]:
        itemRemoved = myQueues[moves[1]].get()
        myQueues[moves[2]].put(itemRemoved)
        i += 1

    for item in myQueues:
        print(item.get())

    return myQueues

def main():
    print("Hello World!")
    myQueues = generate_stacks()

    with open("RearrangementInput.txt", "r") as f:
        for line in f:
            line = line.strip()
            myMove = [int(num) for num in re.findall(r'\d+', line)]
            myFinalQueues = move_crates(myMove, myQueues)
        
    for item in myFinalQueues:
        print("Done!")
        print(item)
     

if __name__ == "__main__":
    main()
        
        







    
