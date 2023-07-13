# 15/15 on CCC grader, passes extra DMOJ cases as well

from collections import deque

# -IMPORTANT- you need this or else TLE
from sys import stdin
input = stdin.readline

nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes+1)]

for _ in range(edges):
    l, s = map(int, input().split())
    graph[l].append(s)
start, end = map(int, input().split())


def is_greater(start, end):
    # return True if start > end
    visited = [False for _ in range(nodes + 1)]
    visited[start] = True
    q = deque([start])
    while q:
        node = q.popleft()

        if node == end:
            return True
        for adj in graph[node]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True  # setting as visited here prevents wasted appends to queue
    return False


if is_greater(start,end):
    print("yes")
elif is_greater(end, start):
    print("no")
else:
    print("unknown")
    