# 2/15, no idea how to actually solve this
# note that we can rotate the array to reduce the number of hardcoded stuff

n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

best = 1


def solve(arr):
    b = 1
    if arr[0][0] + arr[0][1] == arr[1][0] + arr[1][1]:
        b = 2
    if (arr[0][0] + arr[0][1] + arr[1][0]) == arr[1][1] * 3:
        b = 2
    if arr[0][0] + arr[0][1] == arr[1][0] * 2 == arr[1][1] * 2:
        b = 3
    if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
        b = 4
    return b


for _ in range(4):
    best = max(best, solve(arr))
    arr = list(zip(*arr[::-1]))
print(best)

# # S5 group solve
# # N^2 states, N^2 transitions
# # O(N^4)
# #
# # considerations for future optimizations:
# # - break off a piece as soon as we can
# #
# # note: missing edges cases below
#
# from functools import cache
# from itertools import accumulate
# from fractions import Fraction
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(2)]
#
# psa1 = [0] + list(accumulate(arr[0]))
# query1 = lambda l, r: psa1[r + 1] - psa1[l]
# psa2 = [0] + list(accumulate(arr[1]))
# query2 = lambda l, r: psa2[r + 1] - psa2[l]
#
# total = sum(arr[0]) + sum(arr[1])
# nums = n + n
# avg = Fraction(total, nums)
#
#
# @cache
# def solve(i, j):
#     if i == n and j == n:  # finished
#         return 0
#
#     best = 0
#     if i <= j:  # only move top
#         for ni in range(i, n):
#             if Fraction(query1(i, ni), (ni - i + 1)) == avg:
#                 best = max(best, solve(ni + 1, j) + 1)
#
#     if i >= j:  # only move bottom
#         for nj in range(j, n):
#             if Fraction(query2(j, nj), (nj - j + 1)) == avg:
#                 best = max(best, solve(i, nj + 1) + 1)
#
#     for ni in range(i, n):  # move both top and bottom
#         for nj in range(j, n):
#             if i != j and (nj <= i or ni <= j):  # invalid spilt
#                 continue
#             cells = (ni - i + 1) + (nj - j + 1)
#             total = query1(i, ni) + query2(j, nj)
#             if Fraction(total, cells) == avg:
#                 best = max(best, solve(ni + 1, nj + 1) + 1)
#
#             # corner case: cut in middle
#             for mi in range(i+1, ni):
#                 for mii in range()
#                 if Fraction(total - arr[0][mi], cells - 1) == avg and arr[0][mi] == avg:
#                     best= max(best, solve(ni+1, nj+1) + 2)
#             for mj in range(j+1, nj):
#                 if Fraction(total - arr[1][mj], cells - 1) == avg and arr[1][mj] == avg:
#                     best= max(best, solve(ni+1, nj+1) + 2)
#
#     return best
#
#
# print(solve(0, 0))
#
# """
# 4
# 1 1 1 1
# 1 5 1 29
# """
