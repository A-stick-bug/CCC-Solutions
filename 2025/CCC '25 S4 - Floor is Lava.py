# https://dmoj.ca/problem/ccc25s4
# Multi-state Dijkstra's algorithm
#
# Note that directly operating on the graph results in too many transitions
# Visualization: imagine the graph in 3D where the temperature is what 'layer'/height its on
# - you can go to adjacent nodes of the same height
# - you can also go up and down on your current node
# Notice that this virtual graph has O(N + M) nodes/edges so we can directly run Dijkstra's on it

import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline
inf = 1 << 60

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = [defaultdict(list) for _ in range(N + 1)]
temps = [[] for _ in range(N + 1)]
temps[1].append(0)  # starting node
for a, b, c in edges:
    temps[a].append(c)
    temps[b].append(c)
    graph[a][c].append((b, c, 0))  # same layer: no cost
    graph[b][c].append((a, c, 0))
for i in range(1, N + 1):
    temps[i].sort()

# moving between adjacent layers in same node
for node in range(1, N + 1):
    for j in range(len(temps[node]) - 1):
        layer1 = temps[node][j]
        layer2 = temps[node][j + 1]
        graph[node][layer1].append((node, layer2, abs(layer1 - layer2)))
        graph[node][layer2].append((node, layer1, abs(layer1 - layer2)))

dist = [defaultdict(lambda: inf) for _ in range(N + 1)]  # [node][layer]
dist[1][0] = 0

pq = [(0, 1, 0)]
while pq:
    d, cur, layer = heappop(pq)

    if d > dist[cur][layer]:
        continue
    if cur == N:
        print(d)
        sys.exit()

    for adj, adj_layer, cost in graph[cur][layer]:
        new_cost = d + cost
        if dist[adj][adj_layer] > new_cost:
            dist[adj][adj_layer] = new_cost
            heappush(pq, (new_cost, adj, adj_layer))
