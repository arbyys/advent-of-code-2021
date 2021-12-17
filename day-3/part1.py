from aocd import get_data

data = get_data(day=3, year=2021)
data = data.splitlines()

gamma = ""
binariesLength = len(data[0])

for i in range(binariesLength):
    occurences =  {"0": 0, "1": 0}
    for binary in data:
        occurences[binary[i]] += 1
    gamma += max(occurences, key=occurences.get)

epsilon = "".join(["1" if i == "0" else "0" for i in gamma])
print(int(gamma, 2) * int(epsilon, 2))
