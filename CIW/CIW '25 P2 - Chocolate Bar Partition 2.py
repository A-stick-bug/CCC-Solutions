# https://dmoj.ca/problem/ciw25p2
# - Note that Alice can choose any piece any time, even right before Bob's turn
# - Instead of treating it as alternating turns, we think of it as whether Bob can sabotage the current piece
#
# interval dp: [l][r][turn: 0 alice, 1 bob]

from itertools import accumulate

inf = 1 << 30
n = int(input())
arr = list(map(int, input().split()))
psa = [0] + list(accumulate(arr))

dp = [[[-inf] * n for _ in range(n)] for _ in range(2)]
for i in range(n):
    dp[0][i][i] = dp[1][i][i] = arr[i]

for le in range(2, n + 1):
    for l in range(n - le + 1):
        r = l + le - 1

        # Alice's turn, getting the worst of the 2 options since Bob picks which piece to sabotage
        best = psa[r + 1] - psa[l]
        for m in range(l, r):  # [l,m][m+1,r]
            cur = min(
                max(dp[0][l][m], dp[1][m + 1][r]),
                max(dp[1][l][m], dp[0][m + 1][r])
            )
            best = max(best, cur)
        dp[0][l][r] = best

        # Bob's turn, he makes the cut and chooses the worst one
        best = inf
        for m in range(l, r):  # [l,m][m+1,r]
            cur = max(dp[0][l][m], dp[0][m + 1][r])
            best = min(best, cur)
        dp[1][l][r] = max(best, psa[r + 1] - psa[l])  # Alice can also just take the whole thing

print(dp[0][0][n - 1])

"""
Custom test cases
4
-1 1 2 3
6

7
-3 2 1 2 1 2 -3
5
"""

# # recursive code for reference
# from functools import cache
# @cache
# def solve(l, r, turn):
#     if l == r:
#         return arr[l]
#
#     if turn == 0:  # maximize
#         best = psa[r + 1] - psa[l]
#         for m in range(l, r):  # [l,m][m+1,r]
#             cur = min(
#                 max(solve(l, m, 0), solve(m + 1, r, 1)),
#                 max(solve(l, m, 1), solve(m + 1, r, 0))
#             )
#             best = max(best, cur)
#         return best
#
#     else:  # minimize, still alice turn but bob gets to decide the cut
#         best = inf
#         for m in range(l, r):  # [l,m][m+1,r]
#             cur = max(solve(l, m, 0), solve(m + 1, r, 0))
#             best = min(best, cur)
#         return max(best, psa[r + 1] - psa[l])
#
#
# print(solve(0, n - 1, 0))
