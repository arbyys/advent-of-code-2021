from aocd import get_data
from collections import Counter

data = get_data(day=6, year=2021)
data = data.split(",")
data = [*map(int, data)]

fishes = dict(Counter(data))
fishes[-1] = 0

NUMBER_OF_DAYS = 256

for day in range(NUMBER_OF_DAYS):
    for num in range(-1, 8):
        if(fishes.get(num+1) == None):
            fishes[num] = 0
            continue
        fishes[num] = fishes.get(num+1)
    fishes[8] = fishes[-1]
    fishes[6] += fishes[-1]
    fishes[-1] = 0

print(sum(fishes.values()))
