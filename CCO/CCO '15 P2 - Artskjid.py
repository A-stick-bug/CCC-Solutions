# NP problem go brr
# 48/50 using dp, check c++ code for 50/50 solution
from collections import defaultdict

n_nodes, n_roads = map(int, input().split())
graph = [[] for _ in range(n_nodes)]

for _ in range(n_roads):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

res = 0
max_dists = defaultdict(lambda: defaultdict(int))

stack = [(0, 1, 0)]
while stack:
    node, path, dist = stack.pop()
    if node == n_nodes - 1:
        res = max(res, dist)
        continue

    for adj, adj_dist in graph[node]:
        new_dist = dist + adj_dist
        if path & (1 << adj):
            continue

        new_path = path | (1 << adj)

        if new_dist > max_dists[adj][new_path]:
            max_dists[adj][new_path] = new_dist
            stack.append((adj, new_path, new_dist))

print(res)


# # 43/50 test cases, TLE
# n_nodes, n_roads = map(int, input().split())
# graph = [[] for _ in range(n_nodes)]
#
# for _ in range(n_roads):
#     a, b, dist = map(int, input().split())
#     graph[a].append((b, dist))
#
# max_dist = 0
# state = [False for _ in range(n_nodes)]
# state[0] = True
#
# memo = {}  # keep track of already visited paths
# q = [(0, tuple(state), 0)]
# while q:
#     node, path, dist = q.pop()
#     if node == n_nodes - 1:
#         max_dist = max(max_dist, dist)
#         continue
#
#     for adj, adj_dist in graph[node]:
#         new_dist = dist + adj_dist
#         if path[adj]:
#             continue
#
#         new_path = list(path)
#         new_path[adj] = True
#         new_path = tuple(new_path)
#
#         if (adj, new_path) not in memo or new_dist > memo[(adj, new_path)]:
#             memo[(adj, new_path)] = new_dist
#             q.append((adj, new_path, new_dist))
#
# print(max_dist)
