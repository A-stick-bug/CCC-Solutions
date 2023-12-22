# PYTHON IS TOO SLOW< CHECK C++ CODE
#
# dijkstra's algorithm with an extra variable
# for each node, we store the minimum distance to get there with s time in the sun
# similar to https://dmoj.ca/problem/ccc15s4

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
S = int(input())
N, E = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(E):
    a, b, d, sun = map(int, input().split())
    graph[a].append((b, d, sun))
    graph[b].append((a, d, sun))

dist = [[1 << 30] * (S + 1) for _ in range(N)]  # dist[i][s]: shortest path to i after going through the sun for s time
dist[0] = [0] * (S + 1)  # distance to start is always 0

pq = [(0, 0, 0)]  # distance from 0, node, total sun time
while pq:
    d, cur, sun = heappop(pq)
    if cur == N - 1:
        print(d)
        sys.exit()

    for adj, new_dist, new_sun in graph[cur]:
        new_sun *= new_dist
        if sun + new_sun > S:  # too much sun
            continue
        if d + new_dist < dist[adj][sun + new_sun]:  # found shorter path to here
            dist[adj][sun + new_sun] = d + new_dist
            heappush(pq, (d + new_dist, adj, sun + new_sun))

print(-1)
