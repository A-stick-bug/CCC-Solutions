# finding the second-shortest route in a graph (weighted, directed, and cyclic)
# note that the graph is quite sparse, so we use an adjacency list

import heapq
import sys

input = sys.stdin.readline

n_nodes, n_edges = map(int, input().split())

graph = [[] for _ in range(n_nodes + 1)]
for _ in range(n_edges):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


pq = [(0, 1)]
costs = [float('inf') for _ in range(n_nodes + 1)]
costs[1] = 0
costs2 = [float('inf') for _ in range(n_nodes + 1)]

while pq:
    cost, node = heapq.heappop(pq)

    for adj, adj_cost in graph[node]:
        new_cost = cost + adj_cost

        if costs[adj] > new_cost:
            costs2[adj] = costs[adj]
            costs[adj] = new_cost
            heapq.heappush(pq, (new_cost, adj))

        elif costs2[adj] > new_cost and new_cost != costs[adj]:
            costs2[adj] = new_cost
            heapq.heappush(pq, (new_cost, adj))

res = costs2[n_nodes]
if res == float('inf'):
    print(-1)
else:
    print(res)