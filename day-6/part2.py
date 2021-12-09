from aocd import get_data
import numpy as np
import math
import sys
from statistics import linear_regression

data = get_data(day=6, year=2021)
data = data.split(",")
data = [*map(int, data)]

school = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
total = len(data)
for fish in data:
    school[fish] += 1

for day in range(256):

    placeholder = school[0]
    school[0] = school[1]
    school[1] = school[2]
    school[2] = school[3]
    school[3] = school[4]
    school[4] = school[5]
    school[5] = school[6]
    school[6] = school[7]
    school[7] = school[8]
    school[6] += placeholder
    school[8] = placeholder

    total += placeholder

print(total)
