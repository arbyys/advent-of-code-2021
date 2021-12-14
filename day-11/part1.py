from aocd import get_data

data = get_data(day=11, year=2021)
data = data.splitlines()
for index,line in enumerate(data):
    data[index] = list(map(int, data[index]))

for line in data:
    print(line)
