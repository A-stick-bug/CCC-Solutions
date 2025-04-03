# https://dmoj.ca/problem/hkccc15s4
# Connected functional graph (cycle + tree branches)
# Observations:
# - always place the player in the cycle at the start, we can control where it ends up after X seconds
# - place the monster in the farthest tunnel
# - we want the player to end up right in front of the monster when the monster enters the cycle

import sys

sys.setrecursionlimit(100000)

n = int(input())
nxt = [-1] + list(map(int, input().split()))

# for i, v in enumerate(nxt[1:], start=1):  # print graph for visualization
#     print(i, v)

vis = [False] * (n + 1)

# find nodes in the cycle
cur = 1
path = [1]
while True:
    if vis[cur]:
        in_cycle = [False] * (n + 1)  # in_cycle[i]: whether node `i` is in the cycle
        for node in path[path.index(cur):]:
            in_cycle[node] = True
        break
    path.append(cur)
    vis[cur] = True
    cur = nxt[cur]

# print(in_cycle)

# find the longest path going into the cycle

dp = [-1] * (n + 1)  # distance until we reach the cycle from node `i`


def solve(cur):
    if dp[cur] != -1:  # cache
        return dp[cur]
    if in_cycle[cur]:  # base case: reached leaf
        dp[cur] = 0
    else:
        dp[cur] = solve(nxt[cur]) + 1
    return dp[cur]


for i in range(1, n + 1):
    solve(i)

longest = max(dp)
cycle_le = sum(in_cycle)
print(longest * 2 + (cycle_le - 1) * 2)
