from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

with open("input.txt") as file:
    data = file.read().splitlines()

for index,line in enumerate(data):
    data[index] = list(line)

totalRows = len(data)
totalCols = len(data[0])
totalPositions = totalRows*totalCols
nodes = list(range(totalPositions))

g = Graph(totalPositions)

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
    global data
    counter = 0
    for rowIndexLoop,row in enumerate(data):
        for colIndexLoop,col in enumerate(row):
            if((rowIndexLoop == rowIndex) and (colIndexLoop == colIndex)):
                return counter
            counter += 1

for rowIndex,row in enumerate(data):
    for colIndex,col in enumerate(row):
        for dir in ["up", "right", "down", "left"]:
            firstEdge,secondEdge,risk = findAdjacentNodeRisk(rowIndex, colIndex, dir)
            if(firstEdge == None):
                continue
            g.add_edge(firstEdge, secondEdge, risk)
            print("risk from {} to {} is {}".format(firstEdge, secondEdge, risk))


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if(graph.edges[current_vertex][neighbor] != -1):
                distance = graph.edges[current_vertex][neighbor]
                if(neighbor not in graph.visited):
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if(new_cost < old_cost):
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

D = dijkstra(g, 0)
print(D)
