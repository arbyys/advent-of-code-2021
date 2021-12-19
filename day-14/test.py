from aocd import get_data
import math

data = get_data(day=14, year=2021)
#with open("input.txt") as file:
#    data = file.read()

template = data.split("\n\n")[0]
rulesInput = data.split("\n\n")[1].splitlines()

def addOrAppend(pair, quantity):
    if(pair in pairs):
        pairs[pair] += quantity
    else:
        pairs[pair] = quantity

def substractOrRemove(pair, quantity):
    if(pair not in pairs):
        print("error " + pair)
        return
    if(pairs[pair] == 1):
        pairs.pop(pair, None)
    else:
        pairs[pair] -= quantity

rules = {}
pairs = {}

for rule in rulesInput:
    currentRule = rule.split(" -> ")
    rules[currentRule[0]] = currentRule[1]

for i in range(1, len(template)):
    pair = template[i-1]+template[i]
    addOrAppend(pair, 1)

NUMBER_OF_STEPS = 10

for step in range(1,NUMBER_OF_STEPS+1):
    for pair, quantity in pairs.copy().items():
        if(pair not in rules):
            continue
        correspondingLetter = rules[pair]
        addOrAppend(pair[0] + correspondingLetter, quantity)
        addOrAppend(correspondingLetter + pair[1], quantity)
        substractOrRemove(pair, quantity-1)


occurences = {}
for pair, quantity in pairs.items():
    for letter in pair:
        if(letter not in occurences):
            occurences[letter] = quantity
        else:
            occurences[letter] += quantity
occurences[template[-1]] += 1

#print(occurences)
occurences = {k: math.ceil(v/2) for k, v in occurences.items()}
print({k:v for k,v in sorted(occurences.items())})
print(max(occurences.values()) - min(occurences.values()))


# 2350593395481 too low
# 2360298895777
