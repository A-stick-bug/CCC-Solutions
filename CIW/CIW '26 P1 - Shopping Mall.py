# https://dmoj.ca/problem/ciw26p1
# Multi-source 2D BFS

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
dist = [[-1] * (N + 1) for _ in range(K + 1)]

for i in range(1, N + 1):
    if arr[i] == 0:
        q.append((i, 0))
        dist[0][i] = 0

while q:
    cur, itm = q.popleft()
    if itm == K:
        print(dist[itm][cur])
        sys.exit()
    for adj in graph[cur]:
        if arr[adj] == itm + 1:
            if -1 == dist[itm + 1][adj]:
                dist[itm + 1][adj] = dist[itm][cur] + 1
                q.append((adj, itm + 1))
        else:
            if -1 == dist[itm][adj]:
                dist[itm][adj] = dist[itm][cur] + 1
                q.append((adj, itm))
