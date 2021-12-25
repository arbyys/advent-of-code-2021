from aocd import get_data

data = get_data(day=22, year=2021)
data = data.splitlines()

grid = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]

for line in data:
    passed = True
    type = line.split(" ")[0]
    coords = []
    for axis in line.split(","):
        currentCord = [*map(int, axis.split("=")[1].split(".."))]
        for value in currentCord:
            if(value < -50 or value > 50):
                passed = False
        coords.append(currentCord)
    if(passed):
        for xCoord in range(coords[0][0], coords[0][1]+1):
            for yCoord in range(coords[1][0], coords[1][1]+1):
                for zCoord in range(coords[2][0], coords[2][1]+1):
                    if(type == "on"):
                        grid[xCoord][yCoord][zCoord] = 1
                    else:
                        grid[xCoord][yCoord][zCoord] = 0

counter = 0
for x in grid:
    for y in x:
        for z in y:
            if(z == 1):
                counter += 1
print(counter)
