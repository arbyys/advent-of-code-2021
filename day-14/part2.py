from aocd import get_data

data = get_data(day=14, year=2021)

template = data.split("\n\n")[0]
rulesInput = data.split("\n\n")[1].splitlines()

def addOrAppend(pair, quantity):
    if(pair in pairs):
        pairs[pair] += quantity
    else:
        pairs[pair] = quantity

def substractOrRemove(pair, quantity):
    if(pairs[pair] <= 1):
        pairs.pop(pair, None)
    else:
        pairs[pair] -= quantity

rules = {}
pairs = {}
occurences = {}

for rule in rulesInput:
    currentRule = rule.split(" -> ")
    rules[currentRule[0]] = currentRule[1]

for i in range(1, len(template)):
    pair = template[i-1]+template[i]
    addOrAppend(pair, 1)

for char in template:
    if(char not in occurences):
        occurences[char] = 1
    else:
        occurences[char] += 1

NUMBER_OF_STEPS = 40

for step in range(1,NUMBER_OF_STEPS+1):
    for pair, quantity in pairs.copy().items():
        if(pair not in rules):
            continue
        correspondingLetter = rules[pair]
        substractOrRemove(pair, quantity)
        addOrAppend(pair[0] + correspondingLetter, quantity)
        addOrAppend(correspondingLetter + pair[1], quantity)

        if(correspondingLetter not in occurences):
            occurences[correspondingLetter] = quantity
        else:
            occurences[correspondingLetter] += quantity

print(max(occurences.values()) - min(occurences.values()))
