from aocd import get_data

data = get_data(day=11, year=2021)
data = data.splitlines()
for index,line in enumerate(data):
    data[index] = list(map(int, data[index]))

def flash(rowIndex, colIndex):
    if(rowIndex != 0):
        data[rowIndex-1][colIndex] += 1 # top
    if(colIndex != 0):
        data[rowIndex][colIndex-1] += 1 # left
    if(colIndex != len(data[0])-1):
        data[rowIndex][colIndex+1] += 1 # right
    if(rowIndex != len(data)-1):
        data[rowIndex+1][colIndex] += 1 # down
    if((rowIndex != 0) and (colIndex != 0)):
        data[rowIndex-1][colIndex-1] += 1 # top left
    if((colIndex != 0) and (rowIndex != len(data)-1)):
        data[rowIndex+1][colIndex-1] += 1 # down left
    if((rowIndex != len(data)-1) and (colIndex != len(data[0])-1)):
        data[rowIndex+1][colIndex+1] += 1 # down right
    if((rowIndex != 0) and (colIndex != len(data[0])-1)):
        print(rowIndex+1, colIndex+1)
        data[rowIndex-1][colIndex+1] += 1 # top right

for step in range(1, 101):
    data = [[y+1 for y in x] for x in data]
    alreadyFlashed = []
    while True:
        for indexLine,line in enumerate(data):
            for indexOctopus,octopus in enumerate(line):
                if((octopus >= 9) and ([indexLine, indexOctopus] not in alreadyFlashed)):
                    flash(indexLine, indexOctopus)
                    alreadyFlashed.append([indexLine, indexOctopus])

                query = False
                for row in data:
                    for oct in line:
                        if(oct == 9):
                            query = True
                if(not query):
                    break
    for octopusCoords in alreadyFlashed:
        data[octopusCoords[0]][octopusCoords[1]] = 0
    print("==============")
    for line in data:
        print(line)
    print("==============")
