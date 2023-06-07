# 7/15, WA, only works if the hull has 1 hp

from collections import defaultdict
import heapq

hull, n_islands, n_routes = map(int, input().split())
graph = defaultdict(list)

# undirected graph, can be multiple routes between islands
for i in range(n_routes):
    a, b, time, damage = map(int, input().split())
    if damage == 0:
        graph[a].append((time, b))
        graph[b].append((time, a))

start, end = map(int, input().split())

def dijkstra(start, end):
    costs = [float('inf') for _ in range(n_islands+1)]
    costs[start] = 0
    pq = [(0, start)]
    processed = [False for _ in range(n_islands+1)]

    while pq:
        cost, node = heapq.heappop(pq)
        if node in processed or node not in graph:
            continue

        if node == end:
            return costs[end]

        neighbors = graph[node]

        for neighbor_cost,neighbor  in neighbors:
            new_cost = cost + neighbor_cost
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

        processed[node] = True
    return -1


print(dijkstra(start,end))
