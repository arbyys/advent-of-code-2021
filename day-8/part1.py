from aocd import get_data

data = get_data(day=8, year=2021)
data = data.splitlines()
#data = [*map(int, data)]

with open('i.txt') as file:
    data = file.read().splitlines()
    #data = list(map(int, data)) # to int

totalCount = 0
for line in data:
    segments = line.split(" | ")[1]
    for x in segments.split(" "):
        if(len(x) in [2, 3, 4, 7]):
            totalCount += 1

print(totalCount)
