from aocd import get_data
import sys

data = get_data(day=7, year=2021)
data = data.split(",")
data = [*map(int, data)]

fuelUsed = sys.float_info.max
positionAlignedTo = -1

def factorialWithAddition(n):
    f = 1
    for i in range(1, n + 1):
        f += i
    return f

for position in range(min(data), max(data)+1):
    fuelEachIter = 0
    for crab in data:
        fuelEachIter += factorialWithAddition(abs(crab-position))
    if(fuelEachIter < fuelUsed):
        fuelUsed = fuelEachIter
        positionAlignedTo = position
print(fuelUsed)
