import heapq
from aocd import get_data

data = get_data(day=15, year=2021)
data = data.splitlines()

for index,line in enumerate(data):
    data[index] = list(line)

totalRows = len(data)
totalCols = len(data[0])
totalPositions = totalRows*totalCols
nodes = list(range(totalPositions))
graph = {}

def findAdjacentNodeRisk(rowIndex, colIndex, dir):
    global totalRows, totalCols
    current = findElementOrderPosition(rowIndex, colIndex)
    if(dir == "up"):
        rowIndex -= 1
        if(rowIndex < 0):
            return None, None, None
    elif(dir == "right"):
        colIndex += 1
        if(colIndex > totalCols-1):
            return None, None, None
    elif(dir == "down"):
        rowIndex += 1
        if(rowIndex > totalRows-1):
            return None, None, None
    elif(dir == "left"):
        colIndex -= 1
        if(colIndex < 0):
            return None, None, None
    risk = int(data[rowIndex][colIndex])
    adjacent = findElementOrderPosition(rowIndex, colIndex)
    return (current, adjacent, risk)

def findElementOrderPosition(rowIndex, colIndex):
    global totalCols
    return (totalCols * rowIndex + colIndex)

def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

for rowIndex,row in enumerate(data):
    for colIndex,col in enumerate(row):
        for dir in ["up", "right", "down", "left"]:
            firstEdge,secondEdge,risk = findAdjacentNodeRisk(rowIndex, colIndex, dir)
            if(firstEdge == None):
                continue
            if(firstEdge not in graph):
                graph[firstEdge] = {}
            graph[firstEdge][secondEdge] = risk

result = dijkstra(graph, 0)
print(result[len(result)-1])
