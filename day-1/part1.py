from aocd import get_data

data = get_data(day=1, year=2021)
data = data.splitlines()
data = [*map(int, data)]

last = data[0]
count = 0
for i, item in enumerate(data):
    if(i == 0):
        continue
    if(item > last):
        count += 1
    last = item

print(count)
