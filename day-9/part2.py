from aocd import get_data

data = get_data(day=9, year=2021)
data = data.splitlines()
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

sum = 0
for indexRow,row in enumerate(data):
    for indexCol,element in enumerate(row):
        passed = True
        for dir in ["left", "up", "right", "down"]:
            if(not checkAdjancedElement(indexRow, indexCol, dir)):
                passed = False
        if(passed):
            sum += element+1
print(sum)
