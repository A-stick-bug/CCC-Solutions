# no idea why this works, proof by AC

import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

colors = ["G"] * M
vis = [False] * (N + 1)


def solve(cur, parity):
    for adj, edge in graph[cur]:
        if vis[adj]:
            continue
        vis[adj] = True
        colors[edge] = "R" if parity else "B"
        solve(adj, parity ^ 1)


for i in range(1, N + 1):
    if vis[i]:
        continue
    vis[i] = True
    solve(i, 0)

print("".join(colors))
