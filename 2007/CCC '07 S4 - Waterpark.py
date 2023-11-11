# dynamic programming, similar to 2012 S5 but on a graph instead of matrix
# number of ways to get to a node is the sum of the number of ways to get to its parents nodes

import functools

n = int(input())

# note: this is a DAG (no cycles)
parents = [[] for _ in range(n + 1)]

while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    parents[start].append(end)


# DFS search of all paths (no need to keep track of visited because it's a DAG)
# MUST have the cache to avoid computing a node more than one, without this, the time complexity will be exponential
@functools.cache
def find_paths(node):
    if node == n:
        return 1

    total = 0
    for adj in parents[node]:
        total += find_paths(adj)
    return total


print(find_paths(1))
