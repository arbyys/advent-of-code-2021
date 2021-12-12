from aocd import get_data
import math

data = get_data(day=9, year=2021)
data = data.splitlines()
for index,line in enumerate(data):
    data[index] = list(map(int, data[index]))

with open('input.txt') as file:
    data = file.read().splitlines()
    for index,line in enumerate(data):
        data[index] = list(map(int, data[index]))

MAX_NUMBER_POSSIBLE = 9

def checkAdjancedElement(rowIndex, colIndex, direction):
    currentElement = data[rowIndex][colIndex]
    if(direction == "left"):
        elementToCheck = MAX_NUMBER_POSSIBLE+1 if colIndex == 0 else data[rowIndex][colIndex-1]
    elif(direction == "right"):
        elementToCheck = MAX_NUMBER_POSSIBLE+1 if colIndex == len(data[0])-1 else data[rowIndex][colIndex+1]
    elif(direction == "down"):
        elementToCheck = MAX_NUMBER_POSSIBLE+1 if rowIndex == len(data)-1 else data[rowIndex+1][colIndex]
    elif(direction == "up"):
        elementToCheck = MAX_NUMBER_POSSIBLE+1 if rowIndex == 0 else data[rowIndex-1][colIndex]
    if(currentElement < elementToCheck):
        return True
    return False

def findCrossIndexes(rowIndex, colIndex):
    indexesRows = [[rowIndex, colIndex]]
    indexesCols = []
    for dir in range(-1,2,2):
        tempColIndex = colIndex+dir
        while True:
            if((tempColIndex == -1 or tempColIndex == len(data[0])) or data[rowIndex][tempColIndex] == 9):
                break
            indexesRows.append([rowIndex, tempColIndex])
            tempColIndex += dir
    for dir in range(-1,2,2):
        tempRowIndex = rowIndex+dir
        while True:
            if((tempRowIndex == -1 or tempRowIndex == len(data)) or data[tempRowIndex][colIndex] == 9):
                break
            indexesCols.append([tempRowIndex, colIndex])
            tempRowIndex += dir

    return (list(map(list,set(map(tuple,indexesRows)))),list(map(list,set(map(tuple,indexesCols)))))

def findLineIndexes(rowIndex, colIndex, type):
    indexes = [[rowIndex, colIndex]]
    for dir in range(-1, 2, 2):
        if(type == "row"):
            tempColIndex = colIndex+dir
            while True:
                if((tempColIndex == -1 or tempColIndex == len(data[0])) or data[rowIndex][tempColIndex] == 9):
                    break
                indexes.append([rowIndex, tempColIndex])
                tempColIndex += dir
        elif(type == "col"):
            tempRowIndex = rowIndex+dir
            while True:
                if((tempRowIndex == -1 or tempRowIndex == len(data)) or data[tempRowIndex][colIndex] == 9):
                    break
                indexes.append([tempRowIndex, colIndex])
                tempRowIndex += dir
    return (list(map(list,set(map(tuple,indexes)))))


lowPoints = []
for indexRow,row in enumerate(data):
    for indexCol,element in enumerate(row):
        passed = True
        for dir in ["left", "up", "right", "down"]:
            if(not checkAdjancedElement(indexRow, indexCol, dir)):
                passed = False
        if(passed):
            lowPoints.append([indexRow, indexCol])

allLengths = []
for lowPoint in lowPoints:
    print()
    
allLengths.sort()
allLengths = allLengths[-3:]
print(allLengths)
print(math.prod(allLengths))

# too low 1071000
