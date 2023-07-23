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
