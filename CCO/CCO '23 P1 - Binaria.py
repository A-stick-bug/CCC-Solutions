# https://dmoj.ca/problem/cco23p1
#
# As soon as we fix the first K integers, the rest of the string can be constructed from the SMS
# by looking at the difference between adjacent 'windows'
# - Thus, we only look at the restrictions on the first K integers
# - However, we still need to go through the entire array to get restrictions that result from future sums
#
# Note: we are given that the given SMS is valid, so no need to check for contradictions
#
# TC: O(n)

N, K = map(int, input().split())
arr = list(map(int, input().split()))

### MODULAR ARITHMETIC TEMPLATE START ###
MOD = 10 ** 6 + 3
MN = N+1

factorial = [1] * MN  # precompute factorials
for i in range(2, MN):
    factorial[i] = (factorial[i - 1] * i) % MOD

invfact = [1] * MN  # precompute mod inverse of factorials (for comb)
invfact[MN - 1] = pow(factorial[MN - 1], MOD - 2, MOD)
for i in range(MN - 1, 0, -1):
    invfact[i - 1] = (invfact[i] * i) % MOD

comb = lambda n, k: factorial[n] * invfact[k] * invfact[n - k] % MOD if n >= k else 0  # N choose K
### MODULAR ARITHMETIC TEMPLATE END ###

equal = [-1] * N
res = [-1] * N
le = len(arr)

for i in range(le - 1):
    diff = arr[i + 1] - arr[i]
    if diff == 1:  # forced 0 -> 1
        res[i] = 0
        res[i + K] = 1
    elif diff == -1:  # forced 1 -> 0
        res[i] = 1
        res[i + K] = 0
    else:  # forced res[i] = res[i+K]
        equal[i] = i + K

# propagate equalities to the left
for i in reversed(range(N)):
    if i + K < N and equal[i] == i + K:
        res[i] = res[i + K]

free_choice = sum(i == -1 for i in res[:K])
ones = arr[0] - res[:K].count(1)
print(comb(free_choice, ones))

"""
7 3
1 1 2 2 3
"""

#
#
# def window(mask):
#     res = []
#     for i in range(len(mask)-K+1):
#         res.append(sum(mask[i:i + K]))
#     return res
#
# def slow(N, K, arr):
#     def works(mask):
#         res = []
#         for i in range(len(arr)):
#             res.append(sum(mask[i:i + K]))
#         return res == arr
#
#     t = 0
#     for mask in range(1 << N):
#         r = [1 if mask & (1 << i) else 0 for i in range(N)]
#         t += works(r)
#     return (t)
# #
# #
# # MOD = 10 ** 6 + 3
# # N, K = map(int, input().split())
# # arr = list(map(int, input().split()))
# #
# # print(slow(N,K,arr))
#
# def fast(N,K,arr):
#     one = zero = 0  # forced 0 and 1
#     le = len(arr)
#     for i in range(min(K, le - 1)):
#         diff = arr[i+1] - arr[i]
#         if diff == 1:  # forced 0 -> 1
#             zero += 1
#         elif diff == -1:  # forced 1 -> 0
#             one += 1
#
#
#     from math import comb
#     return(comb(K-one-zero, arr[0] - one) %MOD)
#
#
# MOD = 10**18
# for _ in range(10**4):
#     from random import randint
#     K = 3
#     N = 7
#     p = [randint(0,1) for _ in range(N)]
#     arr = window(p)
#     a1 = slow(N,K,arr)
#     a2 = fast(N,K,arr)
#     if a1 != a2:
#         print(a1,a2,N,K,arr)
#        # print(arr)
#         break
