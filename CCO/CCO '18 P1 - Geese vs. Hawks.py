"""
https://dmoj.ca/problem/cco18p1
Basically a longest common subsequence (LCS) problem, but instead of checking for equal letters,
we look at the points scored and W/L to determine if it could be a rivalry game

Also, it may not always be optimal to count a game as a rivalry game just because we can, so also consider skipping

Note: for iterative DP questions, putting your code in a function can speed it up by around x2
"""


def solve():
    n = int(input())
    geese = input()
    geese_score = list(map(int, input().split()))
    hawk = input()
    hawk_score = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            rival = 0
            if geese[i] != hawk[j] and (
                    (geese[i] == "L" and hawk_score[j] > geese_score[i]) or  # potential rivalry game
                    (geese[i] == "W" and hawk_score[j] < geese_score[i])):
                rival = geese_score[i] + hawk_score[j] + dp[i + 1][j + 1]

            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], rival)

    print(dp[0][0])


solve()

# # TLE, recursive memoization solution for reference
# from functools import cache
# import sys
#
# sys.setrecursionlimit(1000000)
#
# n = int(input())
# geese = input()
# geese_score = list(map(int, input().split()))
# hawk = input()
# hawk_score = list(map(int, input().split()))
#
#
# @cache
# def solve(i, j):
#     if i == n or j == n:  # out of letters to compare
#         return 0
#
#     rival = 0
#     if geese[i] != hawk[j] and ((geese[i] == "L" and hawk_score[j] > geese_score[i]) or  # potential rivalry game
#                                 (geese[i] == "W" and hawk_score[j] < geese_score[i])):
#         rival = geese_score[i] + hawk_score[j] + solve(i + 1, j + 1)
#
#     return max(rival, solve(i + 1, j), solve(i, j + 1))  # either skip the hawk's game or the geese's game
#
#
# print(solve(0, 0))
