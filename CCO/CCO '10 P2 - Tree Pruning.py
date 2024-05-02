# https://dmoj.ca/problem/cco10p2
# Knapsack DP on a binary tree
# dp[cur][diff]: minimum number of prunes in cur's subtree to achieve a difference of diff
# note:
# - python allows negative indexing, so we don't need to offset diff
# - we use padding to avoid handling invalid transitions
#
# TC: O(n^3), n states, n^2 transitions

import sys

input = sys.stdin.readline
N, D = map(int, input().split())
graph = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N):
    id, c, nc = map(int, input().split())
    color[id] = c if c == 1 else -1  # turn 0 -> -1 for convenience
    graph[id].extend([int(input()) for _ in range(nc)])

inf = 301
dp = [[inf] * (N * 2 + 5) for _ in range(N)]


def solve(cur):
    dp[cur][0] = 1  # base case: prune cur's subtree
    if len(graph[cur]) == 0:  # root case: leave as it is
        dp[cur][color[cur]] = 0

    for adj in graph[cur]:
        solve(adj)
    if len(graph[cur]) == 1:  # only 1 child to transition from
        for i in range(-N, N):
            dp[cur][i] = min(dp[cur][i], dp[adj][i - color[cur]])

    elif len(graph[cur]) == 2:
        for adj in graph[cur]:  # transition 1: cut off 1 branch
            for i in range(-N, N):
                dp[cur][i] = min(dp[cur][i], dp[adj][i - color[cur]] + 1)

        # transition 2: combine branches, n^2 ways to pair the 2 branches
        adj1, adj2 = graph[cur]
        for i in range(-N, N):
            for j in range(-N, N):
                transition = i + j + color[cur]
                if not (-N <= transition < N):  # invalid state
                    continue
                dp[cur][transition] = min(dp[cur][transition], dp[adj1][i] + dp[adj2][j])


solve(0)
if dp[0][D] == inf:
    print(-1)
else:
    print(dp[0][D])
