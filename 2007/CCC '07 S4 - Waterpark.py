# 15/15, top-down dynamic programming
# number of ways to get to a node is the sum of the number of ways to get to its parents nodes

import functools

n = int(input())

# note: this is a DAG (no cycles)
# basically each edge points the other way around
parents = [[] for _ in range(n+1)]

while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    parents[end].append(start)


# need the cache to avoid computing the paths to a node multiple times
@functools.cache
def find_paths(node):
    if node == 1:
        return 1

    total = 0
    for adj in parents[node]:
        total += find_paths(adj)
    return total


print(find_paths(n))


# # bottom-up solution (less intuitive)
# n = int(input())
# graph = [[] for _ in range(n + 1)]  # no cycles (DAG)
#
# while True:
#     start, end = map(int, input().split())
#     if start == 0 and end == 0:
#         break
#     graph[start].append(end)
#
# dp = [1]
# for x in reversed(range(1, n)):
#     res = 0
#     for y in graph[x]:
#         res += dp[n - y]
#     dp.append(res)
#
# print(dp[-1])
