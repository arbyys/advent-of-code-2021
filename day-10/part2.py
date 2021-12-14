from aocd import get_data

data = get_data(day=10, year=2021)
data = data.splitlines()
#data = [*map(int, data)]


points = {")": 1, "]": 2, "}": 3, ">": 4}
totalCounts = []

openingCharacters = ["(", "[", "{", "<"]
closingCharacters = [")", "]", "}", ">"]
for line in data:
    expectedCharacters = []
    for character in line:
        if(character in openingCharacters):
            expectedCharacters.append(closingCharacters[openingCharacters.index(character)])
            continue
        if(character == expectedCharacters[-1]):
            expectedCharacters.pop()
        else:
            expectedCharacters = []
            break
    if(len(expectedCharacters) != 0):
        totalCountTemp = 0
        expectedCharacters.reverse()
        for resultCharacter in expectedCharacters:
            totalCountTemp *= 5
            totalCountTemp += points[resultCharacter]
        totalCounts.append(totalCountTemp)

totalCounts.sort()
middleIndex = int((len(totalCounts)-1)/2)
print(totalCounts[middleIndex])
