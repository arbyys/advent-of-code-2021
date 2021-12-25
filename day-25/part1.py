from aocd import get_data
import copy

data = get_data(day=25, year=2021)
data = data.splitlines()

for index,line in enumerate(data):
    data[index] = list(line)

alreadyMovedTo = []
alreadyMovedToSwap = []
nextStepPass = False
step = 0
while True:
    workingData = copy.deepcopy(data)
    for type in [">", "v"]:
        alreadyMovedToSwap = []
        for rowIndex,row in enumerate(data):
            for colIndex,col in enumerate(row):
                if(workingData[rowIndex][colIndex] == type):
                    if([rowIndex, colIndex] in alreadyMovedTo):
                        alreadyMovedTo.remove([rowIndex, colIndex])
                        continue
                    if(type == ">"):
                        if((colIndex == len(workingData[0])-1) and (workingData[rowIndex][0] == ".") and ([rowIndex, 0] not in alreadyMovedToSwap)):
                                workingData[rowIndex][colIndex] = "."
                                workingData[rowIndex][0] = ">"
                        elif((colIndex < len(workingData[0])-1) and (workingData[rowIndex][colIndex+1] == ".")):
                            if(colIndex == 0):
                                alreadyMovedToSwap.append([rowIndex, 0])
                            workingData[rowIndex][colIndex] = "."
                            workingData[rowIndex][colIndex+1] = ">"
                            alreadyMovedTo.append([rowIndex, colIndex+1])
                    else:
                        if((rowIndex == len(workingData)-1) and (workingData[0][colIndex] == ".") and ([0, colIndex] not in alreadyMovedToSwap)):
                                workingData[rowIndex][colIndex] = "."
                                workingData[0][colIndex] = "v"
                        elif((rowIndex < len(workingData)-1) and (workingData[rowIndex+1][colIndex] == ".")):
                            if(rowIndex == 0):
                                alreadyMovedToSwap.append([0, colIndex])
                            workingData[rowIndex][colIndex] = "."
                            workingData[rowIndex+1][colIndex] = "v"
                            alreadyMovedTo.append([rowIndex+1, colIndex])

    if(data == workingData):
        print(step+1)
        break
    data = copy.deepcopy(workingData)
    step += 1
