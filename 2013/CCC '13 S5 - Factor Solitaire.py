"""
Greedy algorithm that works backwards
Literally came up with this solution from observing the explanation of sample output 2. (no idea why it works though)

Forwards: C=A*B, c += a, cost += b, end at input
Using this method is too slow because there are too many factors to consider

Backwards (starting from the input): C=A*B, c -= a, cost += b, end at 1
To minimize the cost when working backwards towards 1:
- we must use the largest factor of C as A (and the other factor B, will be the smallest)
- Note: we cannot use C as a factor of C because our goal is to reach 1, not 0

"""


def find_largest_factor(num):
    """Find the largest factor of num that != num"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return num // i
    return 1  # couldn't find any, just subtract 1 from the number


n = int(input())
cost = 0

while n != 1:
    a = find_largest_factor(n)
    b = n // a  # n = a * b
    cost += b - 1  # have to minus one for some reason (again, not sure why)
    n -= a

print(cost)

# # 10/15, DP solution that actually makes sense
# # O(n*sqrt(n)), n states in total, sqrt(n) transitions due to factoring
#
# from math import isqrt
#
# n = int(input())
#
# inf = 1 << 30
# dp = [inf] * (n + 1)
# dp[n] = 0  # base case, our goal is n
#
# for cur in reversed(range(1, n + 1)):
#     for fac in range(1, isqrt(cur) + 1):  # try all possible pairs (a, b)
#         if cur % fac == 0:
#             other = cur // fac
#             if cur + fac <= n:
#                 dp[cur] = min(dp[cur], other + dp[cur + fac])
#             if cur + other <= n:
#                 dp[cur] = min(dp[cur], fac + dp[cur + other])
#
# print(dp[1])

# # recursive version
# @cache
# def solve(cur):
#     if cur > n:  # too big, we can't decrease
#         return 1 << 60
#     if cur == n:
#         return 0
#     best = 1 << 60
#     for fac in range(1, isqrt(cur) + 1):
#         if cur % fac == 0:
#             other = cur // fac
#             best = min(best, other + solve(cur + fac), fac + solve(cur + other))
#
#     return best
#
#
# print(solve(1))
