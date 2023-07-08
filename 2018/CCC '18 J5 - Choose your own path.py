from collections import deque, defaultdict

# graph theory, finding the minimum distance to all nodes using bfs
# keep track of distances using another dictionary

n = int(input())
graph = defaultdict(list)

for i in range(1, n + 1):
    line = input().split()
    graph[str(i)].extend(line[1:])


def bfs(start):
    q = deque([start])
    visited = set()
    distance = {str(i): float('inf') for i in range(1, n + 1)}
    distance[start] = 0

    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)

        for adjacent in graph[node]:
            distance[adjacent] = min(distance[adjacent], distance[node] + 1)
            q.append(adjacent)

    if len(visited) == n:
        print("Y")
    else:
        print("N")
    return distance

d = bfs("1")
min_cost = float('inf')
for node, cost in d.items():
    if not graph[node] and min_cost > cost:
        min_cost = cost

print(min_cost+1)
