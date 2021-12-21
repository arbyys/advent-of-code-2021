from aocd import get_data

data = get_data(day=17, year=2021)
data = data.split(",")

target_x = [*map(int, ("".join(data[0].split("x=")[1]).split("..")))]
target_y = [*map(int, ("".join(data[1].split("y=")[1]).split("..")))]
totalHighestY = -1

x_velocities = range(-200,200)
y_velocities = range(-200,200)

for x_coord in x_velocities:
    for y_coord in y_velocities:
        velocity = [x_coord, y_coord]
        print(velocity)
        position = [0, 0]

        highestY = 0
        step = 0
        while True:
            if((target_x[0] <= position[0] <= target_x[1]) and (target_y[0] <= position[1] <= target_y[1])):
                if(highestY > totalHighestY):
                    totalHighestY = highestY
            if(((position[0] > target_x[1]) or (position[1] < target_y[1])) and step > 100):
                break
            position = [a + b for a, b in zip(position, velocity)]
            if(position[1] > highestY):
                highestY = position[1]
            velocity[0] += 1 if velocity[0] < 0 else (0 if velocity[0] == 0 else -1)
            velocity[1] -= 1
            step += 1

print(totalHighestY)
