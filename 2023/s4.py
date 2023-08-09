# Kruskal's algorithm but reversed, instead of using a disjoint set to check for connection
# we use Dijkstra's algorithm to check if REMOVING an edges increases the distance between the 2 points that it connects
# O(n^2 * log(n)), since N is close to M

import heapq


def distance(start, end):
    pq = [(0, start)]
    distances = [float('inf')] * (n_nodes+1)
    distances[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if node == end:
            return dist

        for adj, adj_dist, _, i in graph[node]:  # cost is ignored
            if i in cannot_use:  # not allowed to use this edge
                continue

            new_dist = dist + adj_dist
            if distances[adj] > new_dist:
                heapq.heappush(pq, (new_dist, adj))
                distances[adj] = new_dist

    return float('inf')  # no path


n_nodes, n_edges = map(int, input().split())
edges = []
graph = [[] for _ in range(n_nodes + 1)]
cannot_use = set()  # a set of 'removed' edges

for i in range(n_edges):
    a, b, dist, cost = map(int, input().split())
    edges.append((a, b, dist, cost, i))  # each edge is given an 'id'
    graph[a].append((b, dist, cost, i))  # both directions are technically the same edge
    graph[b].append((a, dist, cost, i))

# sort by distance, this will guarantee that after we remove edges, the paths will still be shortest
edges.sort(key=lambda x: x[3], reverse=True)

total_cost = 0
for a, b, _, c, id in edges:
    # try REMOVING an edge
    original = distance(a, b)

    cannot_use.add(id)  # check distance without this road
    if distance(a, b) > original:  # we must use this road, otherwise the distance will be longer
        cannot_use.remove(id)
        total_cost += c

print(total_cost)
