from aocd import get_data
import json
import copy
import math
import re
import io
import os

data = get_data(day=18, year=2021)
data = data.splitlines()

def add(firstNumber, secondNumber):
    return [json.loads(firstNumber), json.loads(secondNumber)]

currentNumber = data[0]
alreadySplited = False

def isExplodable(currentNumber):
    currentNumber = str(currentNumber)
    depth = 0
    for item in currentNumber:
        if(item == "["):
            depth += 1
        elif(item == "]"):
            depth -= 1
        if(depth >= 5):
            return True
    return False

def isSplittable(currentNumber):
    currentNumber = str(currentNumber)
    return True if re.search(r'\d\d\d*', currentNumber) else False

def magnitude(currentNumber):
    currentNumber = str(currentNumber)
    while '[' in currentNumber:
        i = 0
        while(i < len(currentNumber)):
            if currentNumber[i].isdigit():
                if((not '[' in currentNumber[i:]) or (currentNumber[i:].index('[') > currentNumber[i:].index(']'))):
                    left, right = [int(x) for x in currentNumber[i : currentNumber.index(']')].split(',')]
                    currentNumber = currentNumber[:i-1] + str(left * 3 + right * 2) + currentNumber[currentNumber.index(']') + 1:]
                    break
            i += 1
    return int(currentNumber)

def remaining_length(buffer):
    current_position = buffer.tell()
    try:
        buffer.seek(0, os.SEEK_END)
        ending_position = buffer.tell()
        return ending_position - current_position
    finally:
        buffer.seek(current_position)

def peek(buffer, n=1):
    position = buffer.tell()
    try:
        return buffer.read(n)
    finally:
        buffer.seek(position)

def explodeNumber(snailfish_number):
    snailfish_number = str(snailfish_number)
    buffer = io.StringIO(snailfish_number)
    stack: list[str] = []
    depth = 0
    exploded = False
    while remaining_length(buffer):
        char = buffer.read(1)
        if(char == "["):
            depth += 1
        elif(char == "]"):
            depth -= 1
        stack.append(char)

        if(depth > 4):
            element = []
            while((c := buffer.read(1)) != "]"):
                element.append(c)
            stack.pop()
            depth -= 1
            left, right = "".join(element).split(",")
            add_val_to_left = len(stack) > 4
            if(add_val_to_left):
                open_count = 0
                close_count = 0
                while(not (c := stack.pop()).isdigit()):
                    if(c == "["):
                        open_count += 1
                    elif(c == "]"):
                        close_count += 1

                value_to_left = [c]
                while stack[-1].isdigit():
                    value_to_left.append(stack.pop())

                value_to_left = int("".join(reversed(value_to_left)))
                stack.append(f"{int(left) + value_to_left}")
                stack.extend("]" for _ in range(close_count))
                stack.append(",")
                stack.extend("[" for _ in range(open_count))

            if(remaining_length(buffer) > 4):
                close_count = 0
                open_count = 0
                while(not (c := buffer.read(1)).isdigit()):
                    if(c == "]"):
                        close_count += 1
                    elif(c == "["):
                        open_count += 1

                value_to_right = [c]
                while(peek(buffer).isdigit()):
                    value_to_right.append(buffer.read(1))

                value_to_right = int("".join(value_to_right))
                stack.append("0")
                stack.extend("]" for _ in range(close_count))
                stack.append(",")
                stack.extend("[" for _ in range(open_count))
                stack.append(f"{int(right) + value_to_right}")

            elif(add_val_to_left):
                stack.append("0")

            stack.extend(buffer.read())
            exploded = True
            break

    return "".join(stack)

def generateSplitNumber(match):
    global alreadySplited
    matched_str = match.group(0)
    num = int(matched_str)
    if((num < 10) or alreadySplited):
        return matched_str
    alreadySplited = True
    return "[{}, {}]".format(math.floor(num/2), math.ceil(num/2))

def splitNumber(currentNumber):
    global alreadySplited
    alreadySplited = False
    currentNumber = str(currentNumber)
    currentNumber = re.sub("[0-9]+", generateSplitNumber, currentNumber)
    return str(currentNumber)

for index in range(1, len(data)):
    currentNumber = add(currentNumber, data[index])
    while True:
        while isExplodable(currentNumber):
            reducedExplode = False
            while(not reducedExplode):
                explodedCurrentNumber = explodeNumber(currentNumber)
                if(currentNumber == explodedCurrentNumber):
                    reducedExplode = True
                else:
                    reducedExplode = False
                currentNumber = explodedCurrentNumber
        if(isSplittable(currentNumber)):
            currentNumber = splitNumber(currentNumber)
        else:
            if(isExplodable(currentNumber)):
                continue
            break

print(magnitude(currentNumber))
