from aocd import get_data

data = get_data(day=5, year=2021)
data = data.splitlines()

highestX = 0
highestY = 0
for instruction in data:
    instruction = instruction.split(" -> ")
    coordsX = [int(instruction[0].split(",")[0]), int(instruction[1].split(",")[0])]
    coordsY = [int(instruction[0].split(",")[1]), int(instruction[1].split(",")[1])]
    if(max(coordsX) > highestX):
        highestX = max(coordsX)
    if(max(coordsY) > highestY):
        highestY = max(coordsY)

grid = []

for x in range(highestY+1):
    grid.append([0]*(highestX+1))

for i,instruction in enumerate(data):
    instruction = instruction.split(" -> ")
    coordsX = [int(instruction[0].split(",")[0]), int(instruction[1].split(",")[0])]
    coordsY = [int(instruction[0].split(",")[1]), int(instruction[1].split(",")[1])]
    if(coordsX[0] == coordsX[1]):
        coordsListX = [coordsX[0]]*(abs(coordsY[0]-coordsY[1])+1)
    else:
        if(coordsX[0] > coordsX[1]):
            coordsListX = list(range(coordsX[0], coordsX[1]-1, -1))
        else:
            coordsListX = list(range(coordsX[0], coordsX[1]+1))
    if(coordsY[0] == coordsY[1]):
        coordsListY = [coordsY[0]]*(abs(coordsX[0]-coordsX[1])+1)
    else:
        if(coordsY[0] > coordsY[1]):
            coordsListY = list(range(coordsY[0], coordsY[1]-1, -1))
        else:
            coordsListY = list(range(coordsY[0], coordsY[1]+1))

    for index in range(len(coordsListX)):
        grid[coordsListY[index]][coordsListX[index]] += 1

totalCount = 0

for row in grid:
    for item in row:
        if(item >= 2):
            totalCount+=1
print(totalCount)
