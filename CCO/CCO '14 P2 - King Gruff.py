# https://dmoj.ca/problem/cco14p2
# Process each edge independently as A -> edge -> B to find the shortest path they are part of
# We can precompute distances from A and B (reversed) to efficiently processes the edges
# For queries, we get the sum of edge costs for edges with shortest path < D

import sys
from bisect import bisect_right
from itertools import accumulate
from collections import deque

input = sys.stdin.readline
inf = 1 << 60

N, M, A, B = map(int, input().split())

graph = [[] for _ in range(N + 1)]
r_graph = [[] for _ in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]
for a, b, l, c in edges:
    graph[a].append((b, l, c))
    r_graph[b].append((a, l, c))

# preprocessing shortest distances from A
q = deque([A])
dist = [inf] * (N + 1)
inq = [False] * (N + 1)
inq[A] = True
dist[A] = 0
while q:
    cur = q.popleft()
    inq[cur] = False
    for adj, le, _ in graph[cur]:
        new_d = dist[cur] + le
        if new_d < dist[adj]:
            dist[adj] = new_d
            if not inq[adj]:
                q.append(adj)

# preprocessing shortest distances from B
q = deque([B])
r_dist = [inf] * (N + 1)
inq = [False] * (N + 1)
inq[B] = True
r_dist[B] = 0
while q:
    cur = q.popleft()
    inq[cur] = False
    for adj, le, _ in r_graph[cur]:
        new_d = r_dist[cur] + le
        if new_d < r_dist[adj]:
            r_dist[adj] = new_d
            if not inq[adj]:
                q.append(adj)

edge_costs = []  # (shortest distance path that edge `i` is part of, cost of edge)
for i in range(M):
    a, b, le, cost = edges[i]
    d = dist[a] + r_dist[b] + le
    edge_costs.append((d, cost))

edge_costs.sort(key=lambda x: x[0])  # by distance
acc_costs = list(accumulate([c for d, c in edge_costs]))

Q = int(input())
for _ in range(Q):
    mx_dist = int(input())
    idx = bisect_right(edge_costs, mx_dist, key=lambda x: x[0]) - 1
    if idx < 0:
        print(0)
    else:
        print(acc_costs[idx])
