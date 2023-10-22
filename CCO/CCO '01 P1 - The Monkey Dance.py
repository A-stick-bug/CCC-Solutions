# https://dmoj.ca/problem/cco01p1
# DFS cycle detection + math trick
#
# First use dfs to detect all cycles and get their length
# The LCM of the cycle lengths is when all monkeys get back to the start
# (It's kind of like the math question where people are running around a track and each person takes a different time
# to run a lap, when do all players meet at the start)

from math import lcm
from functools import reduce


def dfs(cur, d):
    """Use dfs to find the length of a cycle"""
    if dist[cur] != -1:
        return d - dist[cur]  # already visited this node before, get cycle length
    dist[cur] = d
    return dfs(graph[cur], d + 1)


while True:
    n = int(input())
    if n == 0:
        break

    graph = [None] * (n + 1)
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a] = b

    dist = [-1] * (n + 1)  # distances to nodes in the current path, this is how we get the length of cycles
    cycles = []
    for node in range(1, n+1):
        if dist[node] == -1:  # not processed yet
            cycles.append(dfs(node, 0))

    print(reduce(lcm, cycles))  # get lcm of all elements
