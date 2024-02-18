# https://dmoj.ca/problem/ccc11j5
#
# Senior level strategy: Using Tree DP
# - First we notice that the graph is a rooted tree (where Mark be the root)
# - Since we are only going down the tree, we can keep it undirected
# - We are looking for 'the # of ways': multiply answers at children
#
# TC: O(n)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n):
    j = int(input())
    graph[j].append(i)  # j is i's parent


def solve(cur):
    if not graph[cur]:  # leaf node: 2 options, unfriend or don't unfriend
        return 2
    total = 1
    for adj in graph[cur]:
        total *= solve(adj)
    return total + 1  # add the option of removing everything in the subtree


print(solve(n) - 1)  # minus the option of removing everything (Mark can't be removed)

# # Junior level strategy: Brute force all combinations
#
# from itertools import combinations
#
# n = int(input())
# graph = [[] for _ in range(n+1)]  # note: this is a DAG (no cycles)
#
# for i in range(1, n):  # create the graph
#     p = int(input())
#     graph[p].append(i)
#
#
# def dfs(n):  # removing someone will also remove everything else they invited
#     stack = [n]
#     visited = []
#     while stack:
#         node = stack.pop()
#         visited.append(node)
#         stack.extend(graph[node])
#     return visited
#
#
# pieces = []
# for i in range(1, n):
#     pieces.append(dfs(i))
#
# all_combs = []
# for i in range(1, n):
#     all_combs.extend(combinations(pieces, i))
#
# res = 1
# for comb in all_combs:  # if a person appears more than once in a combination, it is not valid
#     valid = True
#     seen = set()
#     for group in comb:
#         for i in group:
#             if i in seen:
#                 valid = False
#                 break
#             else:
#                 seen.add(i)
#     if valid:
#         res += 1
#
# print(res)
