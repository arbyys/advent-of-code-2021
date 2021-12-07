from aocd import get_data
import sys

data = get_data(day=7, year=2021)
data = data.split(",")
data = [*map(int, data)]

fuelUsed = sys.float_info.max
positionAlignedTo = -1

for position in range(min(data), max(data)+1):
    fuelEachIter = 0
    for crab in data:
        fuelEachIter += abs(crab-position)
    if(fuelEachIter < fuelUsed):
        fuelUsed = fuelEachIter
        positionAlignedTo = position

print(fuelUsed)
