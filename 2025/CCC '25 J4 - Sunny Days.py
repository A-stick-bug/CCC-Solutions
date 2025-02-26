# note: a simpler solution may be uploaded later
#
# https://dmoj.ca/problem/ccc25j4
# Dynamic programming, 1-indexed
# Watch out for the edge case!
#
# dp[i][incorrect (t/f)] = consecutive days of sun
# transition: dp[i][j] = dp[i-1][j-p] where p is whether day i has precipitation

import sys

n = int(input())
arr = [-1] + [input() for _ in range(n)]

if all(i == "S" for i in arr[1:]):  # corner case: all sunny, one day is wrong
    print(n - 1)
    sys.exit()

dp = [[0, 0] for _ in range(n + 1)]
for i in range(1, n + 1):
    if arr[i] == "S":
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1] + 1
    else:
        dp[i][1] = dp[i - 1][0] + 1

print(max(max(state) for state in dp))

"""
8
P
S
P
S
S
P
P
S
"""

"""
# braindead psa + binary search approach

from itertools import accumulate


def works(sz):
    return any(psa[i + sz] - psa[i] <= 1 for i in range(n - sz + 1))


n = int(input())
arr = [input() for _ in range(n)]

if all(i == "S" for i in arr):
    print(n - 1)
    import sys

    sys.exit()

psa = [0] + list(accumulate([i == "P" for i in arr]))

low = 0
ans = 0
high = n
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)

"""
