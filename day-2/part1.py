from aocd import get_data

data = get_data(day=2, year=2021)
data = data.splitlines()

coords = [0,0]
for instruction in data:
    command = instruction.split(" ")[0]
    amount = int(instruction.split(" ")[1])

    if(command == "forward"):
        coords[0] += amount
    elif(command == "down"):
        coords[1] += amount
    else:
        coords[1] -= amount

print(coords[0] * coords[1])
