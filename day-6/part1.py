from aocd import get_data

data = get_data(day=6, year=2021)
data = data.split(",")
data = [*map(int, data)]

NUMBER_OF_DAYS = 80

for day in range(1, NUMBER_OF_DAYS+1):
    fishesBorn = 0
    for index,fish in enumerate(data):
        if(fish == 0):
            fishesBorn += 1
            data[index] = 6
        else:
            data[index] = data[index]-1
    for i in range(fishesBorn):
        data.append(8)

print(len(data))
