from aocd import get_data

data = get_data(day=8, year=2021)
data = data.splitlines()

for index,row in enumerate(data):
    temp = []
    temp.append(row.split(" | ")[0].split(" "))
    temp.append(row.split(" | ")[1].split(" "))
    data[index] = temp

lengthOfNumber = [7, 2, 5, 5, 4, 5, 6, 3, 7, 6]
totalSum = 0

def substractStringFromAnother(codeFirst, codeSecond):
    for letter in codeSecond:
        codeFirst = codeFirst.replace(letter,"")
    return codeFirst

for row in data:
    input = row[0]
    output = row[1]
    segmentValues = [""]*7
    numberCodes = [""]*10
    for num in [1, 4, 7, 8]:
        numberCodes[num] = "".join(sorted([item for item in input if len(item)==lengthOfNumber[num]][0]))
    segmentValues[0] = substractStringFromAnother(numberCodes[7], numberCodes[1])
    if("".join(sorted(substractStringFromAnother(numberCodes[8], numberCodes[1][0]))) in [''.join(sorted(i)) for i in input]):
        numberCodes[6] = "".join(sorted(substractStringFromAnother(numberCodes[8], numberCodes[1][0])))
        segmentValues[2] = numberCodes[1][0]
        segmentValues[5] = numberCodes[1][1]
    else:
        numberCodes[6] = "".join(sorted(substractStringFromAnother(numberCodes[8], numberCodes[1][1])))
        segmentValues[2] = numberCodes[1][1]
        segmentValues[5] = numberCodes[1][0]
    for item in input:
        if(len(item) != 5):
            continue
        if(len(substractStringFromAnother(item, segmentValues[0] + segmentValues[2] + segmentValues[5])) == 2):
            numberCodes[3] = "".join(sorted(item))
    segmentValues[1] = substractStringFromAnother(numberCodes[4], numberCodes[3])
    segmentValues[3] = substractStringFromAnother(substractStringFromAnother(numberCodes[4], numberCodes[7]), segmentValues[1])
    segmentValues[4] = substractStringFromAnother(substractStringFromAnother(numberCodes[8], numberCodes[3]), segmentValues[1])
    segmentValues[6] = substractStringFromAnother(substractStringFromAnother(numberCodes[8], numberCodes[4]), segmentValues[1] + segmentValues[4] + segmentValues[0])
    numberCodes[0] = "".join(sorted(substractStringFromAnother(numberCodes[8], segmentValues[3])))
    numberCodes[2] = "".join(sorted(substractStringFromAnother(numberCodes[8], segmentValues[1] + segmentValues[5])))
    numberCodes[5] = "".join(sorted(substractStringFromAnother(numberCodes[8], segmentValues[2] + segmentValues[4])))
    numberCodes[9] = "".join(sorted(substractStringFromAnother(numberCodes[8], segmentValues[4])))

    outputValue = ""
    for item in output:
        outputValue += str(numberCodes.index("".join(sorted(item))))
    totalSum += int(outputValue)

print(totalSum)
