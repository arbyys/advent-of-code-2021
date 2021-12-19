from aocd import get_data

data = get_data(day=12, year=2021)
data = data.splitlines()

with open("input.txt") as file:
    data = file.read().splitlines()

graph = {}
for path in data:
    path = path.split("-")
    if(path[0] in graph):
        graph[path[0]].append(path[1])
    else:
        graph[path[0]] = [path[1]]
    if(path[1] in graph):
        graph[path[1]].append(path[0])
    else:
        graph[path[1]] = [path[0]]

tempGraph = graph.copy()
for key in graph:
    if(key.islower()):
        passed = True
        for item in graph[key]:
            if(item.isupper()):
                passed = False
        if(passed):
            for item in graph[key]:
                tempGraph[item].remove(key)
            tempGraph.pop(key, None)
graph = tempGraph.copy()

totalPaths = 0

def checkNeighbourCaves(cave, cantVisit):
    print("current ", cave)
    print(cantVisit)
    print("===========")
    global totalPaths
    if(cave == "end"):
        totalPaths += 1
        return
    if(cave.islower()):
        cantVisit.append(cave)
    for neighbourCave in graph[cave]:
        if(neighbourCave not in cantVisit):
            checkNeighbourCaves(neighbourCave, cantVisit)

checkNeighbourCaves("start", [])

print(totalPaths)

for key in graph:
    print (key, '->', graph[key])
