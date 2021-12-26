from collections import defaultdict
from aocd import get_data

data = get_data(day=12, year=2021)
data = data.splitlines()

def dfs(currentNode, visited, alreadyInSmall):
    if(currentNode == "end"):
        return True
    elif(visited[currentNode] > 0 and alreadyInSmall):
        return False
    if(currentNode in smallCaves):
        visited[currentNode] += 1
        if(visited[currentNode] == 2):
            alreadyInSmall = True

    pathsCount = 0

    for node in adjacent[currentNode]:
        if(node != "start"):
            pathsCount += dfs(node, visited, alreadyInSmall)

    visited[currentNode] -= 1
    return pathsCount

edges = []
for line in data:
    edges.append(line.split("-"))
adjacent = defaultdict(list)
smallCaves = set()

for edge in edges:
    a = edge[0]
    b = edge[1]
    adjacent[a].append(b)
    adjacent[b].append(a)

    if(a.islower()):
        smallCaves.add(a)
    if(b.islower()):
        smallCaves.add(b)

result = dfs("start", defaultdict(int), False)
print(result)
