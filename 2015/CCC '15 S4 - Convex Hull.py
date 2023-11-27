# using dijkstra's algorithm, extra dimension in the distance array to keep track of damage

import sys
import heapq

input = sys.stdin.readline
hull, n_islands, n_routes = map(int, input().split())
graph = [[] for _ in range(n_islands + 1)]

for _ in range(n_routes):
    a, b, pt, dmg = map(int, input().split())
    graph[a].append((b, pt, dmg))
    graph[b].append((a, pt, dmg))
start, end = map(int, input().split())

inf = 10 ** 9 + 1
dist = [[inf]*201 for _ in range(n_islands + 1)]
for i in range(201):
    dist[start][i] = 0  # dist to start is always 0

pq = [(0, start, 0)]  # (distance, island, damage)

while pq:
    time, island, damage = heapq.heappop(pq)
    if island == end and damage < hull:
        print(time)
        sys.exit()

    for adj, adj_time, adj_damage in graph[island]:
        new_time = time + adj_time
        new_damage = damage + adj_damage

        if new_damage >= hull:  # broken hull, can't take this path
            continue

        if new_time < dist[adj][new_damage]:  # found a shorter path
            dist[adj][new_damage] = new_time
            heapq.heappush(pq, (new_time, adj, new_damage))

print(-1)
