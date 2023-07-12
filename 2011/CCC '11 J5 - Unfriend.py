# 15/15, tricky graph theory

from itertools import combinations

n = int(input())
graph = [[] for _ in range(n+1)]  # note: this is a DAG (no cycles)

for i in range(1, n):  # create the graph
    p = int(input())
    graph[p].append(i)


def dfs(n):  # removing someone will also remove everything else they invited
    stack = [n]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        stack.extend(graph[node])
    return visited


pieces = []
for i in range(1, n):
    pieces.append(dfs(i))

all_combs = []
for i in range(1, n):
    all_combs.extend(combinations(pieces, i))

res = 1
for comb in all_combs:  # if a person appears more than once in a combination, it is not valid
    valid = True
    seen = set()
    for group in comb:
        for i in group:
            if i in seen:
                valid = False
                break
            else:
                seen.add(i)
    if valid:
        res += 1

print(res)
