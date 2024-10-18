"""
https://dmoj.ca/problem/ccc22s3

Observations:
- a cyclic pattern from 1-M e.g. [1,2,3,1,2,3,1,2,3,...] gives the most good samples
- adding an element will make at least 1 good sample

Strategy:
- start with K - N, then add 1 every iteration, so we don't overshoot the good sample amount
  if we have enough good samples, K will be 1 at the start of every iteration so we just add the previous number
- first add as many good samples as possible
- at the end, only add the necessary amount of good samples
"""

import sys

n, m, k = map(int, input().split())

if k < n:  # there are at least n good samples (all numbers are the same)
    print(-1)
    sys.exit()

k -= n
res = []

for i in range(1, n + 1):
    k += 1  # add one by one because adding any number will increase the number of good samples by 1

    if i <= m and i <= k:  # need more samples, add the number that gives the most extra samples
        res.append(i)
        k -= i

    elif i > m and m <= k:  # need more samples, max pitch reached, now cycling through 1 to m
        res.append(m if i % m == 0 else i % m)
        k -= m  # when cycling through 1 to m, you get m new good samples for every note

    else:  # almost right, instead of adding maximum samples, add just the right amount
        res.append(res[-k])
        k = 0

if k != 0:
    print(-1)  # not enough good samples
else:
    print(*res)

# # used for checking if the output is actually correct
#
# from collections import Counter
# def valid_sub(arr):  # could be optimized using sliding window but not worth the effort
#     res = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)+1):
#             sub = Counter(arr[i:j])
#             if all([v == 1 for v in sub.values()]):
#                 res += 1
#     return res
#
# ans = valid_sub(res)
# print(ans == k and max(res) <= m)  # answer is correct or not
# print(ans)
# print("----")
