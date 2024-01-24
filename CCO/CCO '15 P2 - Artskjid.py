# 49/50 using bitmask DP
# Even though the time complexity is exponential, there are still overlapping states so we can use DP
# Instead of storing each state as a list of True/False, we can use a number (0 and 1 in binary) to
# represent if a node has been visited

n_nodes, n_roads = map(int, input().split())
graph = [[] for _ in range(n_nodes)]

for _ in range(n_roads):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

res = 0
max_dists = [[0] * (2 ** 18) for _ in range(n_nodes)]

stack = [(0, 1, 0)]  # current node, path dp state, distance
while stack:
    node, path, dist = stack.pop()
    if node == n_nodes - 1:  # new way to get to end, update answer
        res = max(res, dist)
        continue

    for adj, adj_dist in graph[node]:
        new_dist = dist + adj_dist
        if path & (1 << adj):  # already visited this node on the current path
            continue

        new_path = path | (1 << adj)  # mark as visited in current path

        if new_dist > max_dists[adj][new_path]:  # found better path
            max_dists[adj][new_path] = new_dist
            stack.append((adj, new_path, new_dist))

print(res)

# # 43/50 test cases, TLE
# # store each state as (current node, visited nodes)
#
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
