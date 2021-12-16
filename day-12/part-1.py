from aocd import get_data

data = get_data(day=12, year=2021)
data = data.splitlines()

graph = {}
for instruction in data:
    instruction = instruction.split("-")
    if instruction[0] not in graph:
        graph[instruction[0]] = []

    graph[instruction[0]].append(instruction[1])

def dfs(adj_list, start, target, path, visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            result = dfs(adj_list, neighbour, target, path, visited)
            if result is not None:
                return result
	  path.pop()
    return None

traversal_path = []
traversal_path = dfs(adj_list, 0, 3, traversal_path)
print(traversal_path)
