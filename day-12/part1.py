from collections import defaultdict
from aocd import get_data

data = get_data(day=12, year=2021)
data = data.splitlines()

def dfs(currentNode, visited):
    if(currentNode == "end"):
        return True
    elif(currentNode in visited):
        return False
    elif(currentNode in smallCaves):
        visited.append(currentNode)

    pathsCount = 0

    for node in adjacent[currentNode]:
        pathsCount += dfs(node, visited)

    if(currentNode in visited):
        visited.remove(currentNode)
    return pathsCount

edges = []
for line in data:
    edges.append(line.split("-"))

adjacent = defaultdict(list)
smallCaves = []

for edge in edges:
    a = edge[0]
    b = edge[1]
    if(a.islower()):
        smallCaves.append(a)
    if(b.islower()):
        smallCaves.append(b)

    adjacent[a].append(b)
    adjacent[b].append(a)

result = dfs("start", [])
print(result)
