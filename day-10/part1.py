from aocd import get_data

data = get_data(day=10, year=2021)
data = data.splitlines()
#data = [*map(int, data)]

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
totalCount = 0

openingCharacters = ["(", "[", "{", "<"]
closingCharacters = [")", "]", "}", ">"]
expectedCharacters = []
for line in data:
    for character in line:
        if(character in openingCharacters):
            expectedCharacters.append(closingCharacters[openingCharacters.index(character)])
            continue
        if(character == expectedCharacters[-1]):
            expectedCharacters.pop()
        else:
            totalCount += points[character]
            break

print(totalCount)
