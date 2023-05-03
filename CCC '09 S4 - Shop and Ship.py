# TLE on test cases 4-6

import heapq
from collections import defaultdict

n = int(input())
TRADE_ROUTES = int(input())

graph = defaultdict(list)

for i in range(TRADE_ROUTES):
    node1, node2, cost = list(map(int, input().split()))
    if 0 < node1 <= n and 0 < node2 <= n:
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

p = int(input())
pencils = {i: float('inf') for i in range(1,n+1)}
for i in range(p):
    pencil, cost = list(map(int, input().split()))
    pencils[pencil] = cost

END = int(input())


def shortest_path(start, graph):
    costs = {node: float('inf') for node in range(1,n+1)}
    costs[start] = 0
    pq = [(0, start)]
    processed = set()

    while pq:
        cost, node = heapq.heappop(pq)
        if node in processed:
            continue

        neighbors = graph[node]

        if neighbors is not None:
            for neighbor, neighbor_cost in neighbors:
                new_cost = cost + neighbor_cost
                if costs[neighbor] > new_cost:
                    costs[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        processed.add(node)
    return costs


min_cost = float('inf')
dijkstra_result = shortest_path(END, graph)
for node, cost in dijkstra_result.items():
    if pencils[node] + cost < min_cost:
        min_cost = pencils[node] + cost
print(min_cost)
