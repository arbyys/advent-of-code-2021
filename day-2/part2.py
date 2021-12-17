from aocd import get_data

data = get_data(day=2, year=2021)
data = data.splitlines()

coords = [0,0,0]
for instruction in data:
    command = instruction.split(" ")[0]
    amount = int(instruction.split(" ")[1])

    if(command == "forward"):
        coords[0] += amount
        coords[1] += coords[2] * amount
    elif(command == "down"):
        coords[2] += amount
    else: # up
        coords[2] -= amount

print(coords[0] * coords[1])
