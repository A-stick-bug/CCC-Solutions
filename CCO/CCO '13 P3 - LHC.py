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
    freq = {}
    for path in paths:
        if diameter - path[0] in freq:
            total += path[1] * freq[diameter - path[0]]
        if path[0] not in freq:
            freq[path[0]] = 0
        freq[path[0]] += path[1]
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
