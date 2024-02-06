"""
10/15, PYTHON IS TOO SLOW, CHECK C++ CODE
https://dmoj.ca/problem/ccc15s5

Extension of the house robber question, you can't take 2 pies in a row.
However, you are also given M pies that you can insert anywhere in the list.

For 40%, we can just try inserting M into every possible position.
For full marks, we consider the 5 options at each position (shown in solve function).

Note:
- we must sort the extra pieces so the ones we use as filling are the worst ones and the ones we actually
  take are the best. This is also the reason we need an extra DP state.
- k can actually become -1 (meaning we ran out of pies to insert) but python's negative indexing takes care of this
"""

import sys

inf = 1 << 60
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
pie = [int(input()) for _ in range(N)]
M = int(input())
extra = [int(input()) for _ in range(M)]
extra.sort()
extra.append(0)  # padding for negative indexing

cache = [[[-1] * (M + 1) for _ in range(M + 2)] for _ in range(N)]


# 10/15, recursion is too slow (at least for python)
def solve(i, j, k):
    if j - k > 1:  # invalid state
        return -inf
    if i >= N:  # finished
        return 0
    if cache[i][j][k] != -1:
        return cache[i][j][k]

    cache[i][j][k] = max(solve(i + 1, j, k),  # skip pie
                         solve(i + 2, j, k) + pie[i],  # take pie
                         solve(i + 1, j + 1, k) + pie[i],  # take, use extra pie as filling so we can take 2 in a row
                         solve(i + 1, j, k - 1) + extra[k],  # add extra pie, skip normal
                         solve(i, j + 1, k - 1) + extra[k])  # add extra pie, also use an extra pie as filling
    return cache[i][j][k]


print(solve(0, 0, M - 1))

# # 6/15, brute force
# def solve(arr):
#     dp = [0] * len(arr)
#     dp[0] = arr[0]  # base cases
#     dp[1] = max(arr[0], arr[1])
#
#     for i in range(2, len(arr)):
#         dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
#     return dp[-1]
#
#
# if M == 0:
#     if N == 1:
#         print(pie[0])
#     print(solve(pie))
#
# elif M == 1:
#     best = 0
#     for i in range(N + 1):  # try all possible positions to insert pie
#         new_arr = pie.copy()
#         new_arr.insert(i, extra[0])
#         best = max(best, solve(new_arr))
#     print(best)
