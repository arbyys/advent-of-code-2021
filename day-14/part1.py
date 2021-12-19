from aocd import get_data

data = get_data(day=14, year=2021)

template = list(data.split("\n\n")[0])
rules = data.split("\n\n")[1].splitlines()

matchingLetters = []
appendingLetters = []

for rule in rules:
    currentRule = rule.split(" -> ")
    matchingLetters.append(currentRule[0])
    appendingLetters.append(currentRule[1])

NUMBER_OF_STEPS = 10
for step in range(1, NUMBER_OF_STEPS+1):
    workingTemplate = template.copy()
    workingIndex = 0
    for index,letter in enumerate(template):
        if(index >= len(template)-1):
            break
        nextLetter = template[index+1]
        if(letter+nextLetter in matchingLetters):
            indexOfLetter = matchingLetters.index(letter+nextLetter)
            workingTemplate.insert(workingIndex+1, appendingLetters[indexOfLetter])
            workingIndex += 1
        workingIndex += 1
    template = workingTemplate.copy()

occurences = {}
for letter in template:
    if(letter not in occurences):
        occurences[letter] = 1
        continue
    occurences[letter] += 1

print({k:v for k,v in sorted(occurences.items())})
print(max(occurences.values()) - min(occurences.values()))
