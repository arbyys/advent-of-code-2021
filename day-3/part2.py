from aocd import get_data

data = get_data(day=3, year=2021)
data = data.splitlines()
#data = [*map(int, data)]

generator = ""
scrubber = ""
binariesLength = len(data[0])

def searchData(givenData, mostCommon):
    tempArray = []
    dataFunc = givenData.copy()
    while True:
        for i in range(binariesLength):
            if(len(tempArray) > 0):
                dataFunc = tempArray.copy()
            tempArray = []
            occurences = {"0": 0, "1": 0}
            for binary in dataFunc:
                occurences[binary[i]] += 1
            for z,binary in enumerate(dataFunc):
                if(int(occurences["0"]) == int(occurences["1"])):
                    bitToKeep = int(mostCommon)
                else:
                    bitToKeep = int(max(occurences, key=occurences.get) if mostCommon else min(occurences, key=occurences.get))
                if((int(binary[i]) == bitToKeep)):
                    tempArray.append(binary)
            if(len(dataFunc) <= 1):
                return dataFunc[0]



generator = searchData(data, True)
scrubber = searchData(data, False)
print(int(generator, 2), int(scrubber, 2))
print(int(generator, 2) * int(scrubber, 2))
