# https://dmoj.ca/problem/ciw26p3
# compute https://oeis.org/A063655

import sys
from math import isqrt

n = int(input())
if n == 0:
    print(0)
    sys.exit()

best = float("inf")
for i in range(1, isqrt(n) + 1):
    if n % i == 0:
        best = min(best, i + n // i)
print(best)


# observation stuff
# import sys
# from functools import cache
#
# inf = 1<<60
# def solve(n):
#     @cache
#     def maximize(A,B):
#         if A +B == n:
#             return 0
#         return max(maximize(A+1, B) + B, maximize(A, B+1) + A )
#
#     return maximize(0, 0)
#
# res = []
# N = int(input())
# for i in range(1, 1000):
#
#     res.append(solve(i))
#     print(res[-1])
#     if N <= res[-1]:
#         print(i)
#         sys.exit()
#
# #print(res)

#
# import sys
# from functools import cache
#
# inf = 1<<60
# def solve(n):
#     @cache
#     def maximize(A,B, rest):
#         if A > n or B > n:
#             return inf
#         if rest < 0:
#             return inf
#         if rest == 0:
#             return 0
#         return min(maximize(A+1, B, rest-B) + 1, maximize(A, B+1, rest-A) + 1)
#
#     return maximize(0, 0, n)
#
# #print(solve(int(input())))
# res = []
# #N = int(input())
# for i in range(500):
#
#     res.append(solve(i))
#     print(res[-1])
# print(res)
# print(list(range(500)))
# from matplotlib import pyplot as plt
#
# plt.plot(res)
# plt.show() # looks like this has to do with divisors
