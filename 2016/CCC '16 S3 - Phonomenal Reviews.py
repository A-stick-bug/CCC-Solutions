# Q: given a tree, find the shortest path that goes through all nodes in a set
# easier version: https://dmoj.ca/problem/sleigh
# first, we need to remove branches without pho restaurants because you will never go through them
# after doing this, all pho nodes will be at leaves (knowing how to do this is the hard part)

N, M = map(int, input().split())
pho = set(map(int, input().split()))

graph = [set() for _ in range(N)]  # create graph from input
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# start pruning the leaves until we reach a pho or end of branch
for node in range(N):
    while len(graph[node]) == 1 and node not in pho:  # leaves only have 1 connection
        prev = node
        node = list(graph[node])[0]
        graph[prev].remove(node)  # remove connection, leaf is moved to the next node
        graph[node].remove(prev)


def farthest(start):
    dist = [-1] * N
    dist[start] = 0
    stack = [(start, -1)]
    while stack:
        cur, prev = stack.pop()
        for adj in graph[cur]:
            if adj != prev:
                stack.append((adj, cur))
                dist[adj] = dist[cur] + 1
    far = max(dist)
    return far, dist.index(far)  # (max length from start, farthest node from start)


# get diameter, start from a pho node because we know it hasn't been pruned
_, end1 = farthest(list(pho)[0])
diameter, end2 = farthest(end1)

node_count = sum(len(u) != 0 for u in graph)  # number of nodes in the tree after pruning
total = (node_count - 1) * 2  # length to go to every node, every edge is taken exactly twice

# since we don't have to get back to start, we can go through the edges in the diameter only once and save the most time
print(total - diameter)
