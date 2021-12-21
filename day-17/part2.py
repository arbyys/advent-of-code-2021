from aocd import get_data

data = get_data(day=17, year=2021)
data = data.split(",")

target_x = [*map(int, ("".join(data[0].split("x=")[1]).split("..")))]
target_y = [*map(int, ("".join(data[1].split("y=")[1]).split("..")))]

x_velocities = range(-300,300)
y_velocities = range(-300,300)

totalCount = 0

for x_coord in x_velocities:
    for y_coord in y_velocities:
        velocity = [x_coord, y_coord]
        print(velocity)
        position = [0, 0]

        step = 0
        while True:
            if((target_x[0] <= position[0] <= target_x[1]) and (target_y[0] <= position[1] <= target_y[1])):
                totalCount += 1
                break
            if(((position[0] > target_x[1]) or (position[1] < target_y[1])) and step > 200):
                break
            position = [a + b for a, b in zip(position, velocity)]
            velocity[0] += 1 if velocity[0] < 0 else (0 if velocity[0] == 0 else -1)
            velocity[1] -= 1
            step += 1

print(totalCount)
