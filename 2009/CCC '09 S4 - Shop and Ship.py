"""
This problem has few nodes and A LOT of edges so V^2 is actually faster than E*log(V) with heap

After getting the distances to each node from the start, we just take the minimum after adding pencil cost
"""

import sys
from heapq import heappush, heappop

inf = 1 << 50
input = sys.stdin.readline


# def dijkstra(graph, start):  # without heap
#     dist = [inf] * n
#     dist[start] = 0
#     vis = [False] * n
#
#     for _ in range(n):  # n nodes in total, find shortest path to all of them
#         min_distance = inf
#         for i in range(n):
#             if not vis[i] and dist[i] < min_distance:
#                 u = i
#                 min_distance = dist[i]
#         vis[u] = True
#         for k in range(n):
#             if not vis[k] and graph[u][k] and dist[u] + graph[u][k] < dist[k]:
#                 dist[k] = dist[u] + graph[u][k]
#
#     return dist


def dijkstra(graph, start):  # with heap
    dist = [inf] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, cur = heappop(pq)
        if dist[cur] < d:
            continue
        for adj, adj_d in enumerate(graph[cur]):
            new_d = adj_d + d
            if new_d < dist[adj]:
                dist[adj] = new_d
                heappush(pq, (new_d, adj))

    return dist


n = int(input()) + 1
t = int(input())

mat = [[inf] * n for i in range(n)]
# create the adjacency matrix
for i in range(t):
    a, b, c = map(int, input().split())
    # undirected graph
    mat[a][b] = c
    mat[b][a] = c

# consider cost of buying pencil
pencils = int(input())

# (node, cost to buy pencil here)
stores = []
for _ in range(pencils):
    stores.append(list(map(int, input().split())))

start = int(input())
distances = dijkstra(mat, start)  # single source shortest path

# min cost, including the distance
pencil = float('inf')
for d, c in stores:
    pencil = min(pencil, distances[d] + c)

print(pencil)
