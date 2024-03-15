"""
https://dmoj.ca/problem/cco07p6

Q: how many edges/connections do we need to add for every node to be in a single biconnected component

- Use tarjan's algorithm to compress biconnected components into a single node
- Now we have a tree
- Observe that if we connect all leafs of the resulting tree in pairs, we get a single BCC
- If there are an odd number of leaves, just connect the single one to any other leaf
- In total, we always take ceil(LEAVES/2) extra connections

Note:
- Tarjan's algorithm for finding BCC is basically a mix of finding SCC and finding bridges
- For some reason the question has very low constraints. You can probably brute force the BCC part
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)


def get_bcc(graph):
    n = len(graph)

    bcc = [-1] * n  # the component that node i belongs to
    comp = 1  # current component
    low_link = [-1] * n  # smallest time reachable of a node reachable from the DFS subtree of node i
    node_id = [-1] * n  # time at which node i was discovered
    time = 0
    path = []  # nodes currently in the dfs traversal
    in_path = [False] * n

    def dfs(cur, prev):
        nonlocal time, comp
        node_id[cur] = low_link[cur] = time
        path.append(cur)
        in_path[cur] = True
        time += 1

        for adj in graph[cur]:
            if adj == prev:
                continue
            if node_id[adj] == -1:  # not yet visited
                dfs(adj, cur)
                low_link[cur] = min(low_link[cur], low_link[adj])

            else:  # back edge, since we arrived at a node on the current path
                low_link[cur] = min(low_link[cur], node_id[adj])

        if node_id[cur] == low_link[cur]:  # root in dfs tree, assign bcc values to everything in this bcc
            while True:
                in_path[path[-1]] = False
                bcc[path[-1]] = comp
                if path.pop() == cur:
                    break
            comp += 1

    for i in range(1, n):
        if node_id[i] == -1:
            dfs(i, -1)
    return bcc


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bcc = get_bcc(graph)  # compress BCCs into a single node
tree = [set() for _ in range(max(bcc) + 1)]
for i in range(1, len(graph)):
    for adj in graph[i]:
        if bcc[i] != bcc[adj]:
            tree[bcc[i]].add(bcc[adj])

leaves = sum(len(tree[i]) == 1 for i in range(1, len(tree)))
print((leaves + 1) // 2)
