from aocd import get_data

data = get_data(day=12, year=2021)
data = data.splitlines()

graph = {}
pointers = {}

for i,instruction in enumerate(data):
    instruction = instruction.split("-")
    if instruction[0] not in graph:
        graph[instruction[0]] = []
    for subInstruction in instruction[1]:
        if(subInstruction not in graph):
            graph[subInstruction] = []
    graph[instruction[0]].append(instruction[1])
    for subInstruction in instruction[1]:
            graph[subInstruction].append(instruction)

for i, (key, value) in enumerate(graph.items()):
   print(i, key, value)

visitedList = [[]]

def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())
    visitedList.append(visited)

depthFirst(graph, "start", [])

print(visitedList)
