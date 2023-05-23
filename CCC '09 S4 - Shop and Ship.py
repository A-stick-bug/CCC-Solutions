"""
This problem has few nodes and A LOT of edges so V^2 is actually faster than E*log(V) with heap

Since the nodes are numbers 1 to N, we can use a list to keep track of shortest to a node where the value is the cost
and the index is the node (no need for dictionaries)

However, we must add an extra index at the end because arrays indices go from 0 to N-1 and the nodes are numbered 1 to N
Index 0 being there won't affect anything
"""


def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0

    for _ in range(n):
        min_distance = float('inf')
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                u = i
                min_distance = distances[i]
        visited[u] = True
        for k in range(n):
            if not visited[k] and graph[u][k] and distances[u] + graph[u][k] < distances[k]:
                distances[k] = distances[u] + graph[u][k]
    return distances


n = int(input()) + 1
t = int(input())

# for some reason using float('inf') here is slower than 10**9 (greater than max cost possible)
mat = [[10**9 for j in range(n)] for i in range(n)]

# create the adjacency matrix
for i in range(t):
    d, b, c = map(int, input().split())
    # undirected graph
    mat[d][b] = c
    mat[b][d] = c

pencils = int(input())
distances = [float('inf') for i in range(n)]  # distance to each node, the index being the node

# pencil costs in tuple pairs (node, cost to buy pencil here)
stores = []
for _ in range(pencils):
    stores.append(list(map(int, input().split())))

start = int(input())
distances = dijkstra(mat,start)

# adding the node's cost
pencil = float('inf')
for d, c in stores:
    pencil = min(pencil, distances[d] + c)

print(pencil)
