from aocd import get_data

data = get_data(day=1, year=2021)
data = data.splitlines()
data = [*map(int, data)]

last = data[0] + data[1] + data[2]
count = 0
for i, item in enumerate(data):
    if(i == 0):
        continue
    if(i+3 > len(data)):
        break
    current = data[i] + data[i+1] + data[i+2]
    if(current > last):
        count += 1
    last = current

print(count)
