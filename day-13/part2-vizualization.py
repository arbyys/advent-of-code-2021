from aocd import get_data
import time
import os

data = get_data(day=13, year=2021)

instructions = data.split("\n\n")[1].splitlines()
data = data.split("\n\n")[0].splitlines()

def reverseList(axis, list):
    tempList = list.copy()
    if(axis == "y"):
        tempList.reverse()
    else:
        for rowIndex,row in enumerate(tempList):
            tempList[rowIndex].reverse()
    return tempList

def splitGrid(axis, number):
    firstHalf,secondHalf = [],[]
    if(axis == "x"):
        for index,row in enumerate(grid):
            firstHalf.append(row[:number])
            secondHalf.append(row[number+1:])
    elif(axis == "y"):
        for index,row in enumerate(grid):
            if(index == number):
                continue
            if(index > number):
                secondHalf.append(row)
                continue
            firstHalf.append(row)
    return firstHalf, secondHalf

numberOfRows = int(instructions[1].split(" ")[2].split("=")[1])*2
numberOfCols = int(instructions[0].split(" ")[2].split("=")[1])*2

grid = []
for x in range(numberOfRows+1):
    grid.append([0]*(numberOfCols+1))
for coords in data:
    current = [*map(int, coords.split(","))]
    grid[current[1]][current[0]] = 1

for numInstruction,instruction in enumerate(instructions):
    current = instruction.split(" ")[2].split("=")
    firstHalf, secondHalf = splitGrid(current[0], int(current[1]))
    secondHalf = reverseList(current[0], secondHalf)

    mergedList = []

    for rowIndex in range(len(firstHalf)):
        currentRow = []
        for colIndex in range(len(firstHalf[0])):
            currentRow.append(firstHalf[rowIndex][colIndex] + secondHalf[rowIndex][colIndex])
        mergedList.append(currentRow.copy())

    grid = mergedList.copy()
    tempGrid = grid.copy()

    if(numInstruction <= 5):
        continue
    time.sleep(0.5)
    os.system('cls')
    for rowIndex,row in enumerate(tempGrid):
        for colIndex,col in enumerate(row):
            if(col >= 1):
                print("#", end="")
            else:
                print(".", end="")
        print()
input("")