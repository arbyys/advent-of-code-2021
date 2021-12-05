from aocd import get_data

data = get_data(day=4, year=2021)
data = data.split("\n\n")
numbers = [*map(int, data.pop(0).split(","))]

SIZE_OF_BINGO = 5

for index,item in enumerate(data):
    tempList = []
    for line in item.split("\n"):
        oneRow = [*map(int, (' '.join(line.split())).split())]
        tempList.append(oneRow)
    data[index] = tempList

def calculateFinalScore(grid, winningNumber):
    totalSum = 0
    for row in grid:
        for num in row:
            if(num == -1):
                continue
            totalSum += num
    return (totalSum * winningNumber)

def checkForWinner(grid):
    for row in grid:
        if(len(set(row)) < 2):
            return True
    for colIndex in range(SIZE_OF_BINGO):
        colList = []
        for rowIndex in range(SIZE_OF_BINGO):
            colList.append(grid[rowIndex][colIndex])
        if(len(set(colList)) < 2):
            return True
    return False

for drawn in numbers:
    for grid in data:
        for row in grid:
            for i,number in enumerate(row):
                if(drawn == number):
                    row[i] = -1
                if(checkForWinner(grid)):
                    print(calculateFinalScore(grid, drawn))
                    exit()
