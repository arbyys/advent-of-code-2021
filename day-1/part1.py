from aocd import get_data

data = get_data(day=1, year=2021)
data = data.splitlines()
data = [*map(int, data)]

last = data[0]
count = 0

for i in range(1, len(data)):
    if(data[i] > last):
        count += 1
    last = data[i]

print(count)
