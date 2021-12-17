from aocd import get_data
import math

data = get_data(day=9, year=2021)
data = data.splitlines()


for index,line in enumerate(data):
    data[index] = list(map(int, data[index]))

MAX_NUMBER_POSSIBLE = 9

def findLowPoint(rowIndex, colIndex, direction):
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

def searchNeighbours(rowIndex, colIndex):
    if((rowIndex < 0) or (rowIndex > len(data)-1) or (colIndex < 0) or (colIndex > len(data[0])-1)):
        return
    if((data[rowIndex][colIndex] < 9) and ([rowIndex, colIndex] not in alreadySearched)):
        alreadySearched.append([rowIndex, colIndex])
        searchNeighbours(rowIndex-1, colIndex)
        searchNeighbours(rowIndex, colIndex-1)
        searchNeighbours(rowIndex+1, colIndex)
        searchNeighbours(rowIndex, colIndex+1)
    else:
        return

lowPoints = []
basinSizes = []
for indexRow,row in enumerate(data):
    for indexCol,element in enumerate(row):
        passed = True
        for dir in ["left", "up", "right", "down"]:
            if(not findLowPoint(indexRow, indexCol, dir)):
                passed = False
        if(passed):
            lowPoints.append([indexRow, indexCol])

for lowPoint in lowPoints:
    alreadySearched = []
    searchNeighbours(lowPoint[0], lowPoint[1])
    basinSizes.append(len(alreadySearched))

basinSizes.sort()
print(math.prod(basinSizes[-3:]))
