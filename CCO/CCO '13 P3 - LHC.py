"""
Problem: find the distance between the 2 furthest points in a tree and how many times that distance appears
Using tree DP
(using only dfs could also work, but I don't really understand that)

Approach:
1. Find the diameter of the tree using 2 DFS method
2. Start at an arbitrary node, get every path down the tree from the current node and check how many of these paths
   form the length of the diameter when added together (using 2-Sum method)
3. We also need to add the paths starting from the root that are the same length as the diameter by themselves

"""

import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    stack = [start]  # cur, prev
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if dist[adj] == -1:
                stack.append(adj)
                dist[adj] = dist[cur] + 1
    highest = max(dist)
    return highest, dist.index(highest)


_, end1 = dfs(1)  # get diameter using dfs
diameter, end2 = dfs(end1)


def match_branches(paths):
    """finds how many ways you can join 2 branches together to get the diameter (literally 2-Sum)"""
    total = 0
    freq = defaultdict(int)
    for path, cnt in paths:
        if diameter - path in freq:
            total += cnt * freq[diameter - path]
        freq[path] += cnt
    return total


def solve(cur, prev):
    global joined
    paths = []
    for adj in graph[cur]:  # get paths down the tree
        if adj == prev:
            continue
        dist, times = solve(adj, cur)
        dist += 1  # include current node in the path
        paths.append((dist, times))

    if not paths:
        return 0, 1  # leaf node: max dist of 0, appears 1 time

    joined += match_branches(paths)

    # get the longest path down and how many times it appears
    highest = occur = 0
    for d, c in paths:
        if d > highest:
            highest = d
            occur = c
        elif d == highest:
            occur += c
    return highest, occur


res = 0
joined = 0  # diameters formed from joining 2 paths

best, times = solve(1, 0)
if best == diameter:
    joined += times  # paths formed by only going down 1 path

print(diameter + 1, joined)

# # (TLE) alternate approach using centroid decomp (slower but more template)
# from collections import defaultdict
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# size = [0] * (n + 1)
# cut = [False] * (n + 1)  # determine is node i is removed
#
# longest_ans = 0
# ans_count = 1
#
# def get_sizes(cur, prev):
#     """get subtree sizes of a subtree/component"""
#     size[cur] = 1
#     for adj in graph[cur]:
#         if adj == prev or cut[adj]:
#             continue
#         get_sizes(adj, cur)
#         size[cur] += size[adj]
#
#
# def get_centroid(cur, prev, comp_size):
#     """find the centroid of a subtree/component"""
#     for adj in graph[cur]:
#         if not cut[adj] and adj != prev and size[adj] > comp_size // 2:
#             return get_centroid(adj, cur, comp_size)
#     return cur
#
#
# def get_longest_count(cur, prev):
#     stack = [(cur, prev, 0)]  # get the longest path and how many times it appears in a subtree
#     dists= []
#     while stack:
#         cur, prev, d = stack.pop()
#         dists.append(d)
#         for adj in graph[cur]:
#             if adj != prev and not cut[adj]:
#                 stack.append((adj, cur, d + 1))
#     return max(dists), dists.count(max(dists))
#
#
# def solve(root):
#     global longest_ans, ans_count
#     get_sizes(root, -1)
#     if size[root] == 1:  # can't decompose further
#         return
#     root = get_centroid(root, -1, size[root])
#
#     paths = [(0, 1)]  # include empty path
#     for adj in graph[root]:  # get subtree lengths
#         if not cut[adj]:
#             max_dist, dist_count = get_longest_count(adj, root)
#             paths.append((max_dist + 1, dist_count))
#
#     paths.sort()
#     max_joined = paths[-1][0] + paths[-2][0]  # join 2 longest paths
#     total_cnt = 0
#     match = defaultdict(int)
#     for le, cnt in paths:
#         if max_joined - le in match:
#             total_cnt += match[max_joined - le] * cnt
#         match[le] += cnt
#
#     if max_joined > longest_ans:  # update answer
#         longest_ans = max_joined
#         ans_count = total_cnt
#     elif max_joined == longest_ans:
#         ans_count += total_cnt
#
#     # decompose tree
#     cut[root] = True
#     for adj in graph[root]:
#         if not cut[adj]:
#             solve(adj)
#
# solve(1)
# print(longest_ans + 1, ans_count)
