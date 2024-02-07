"""
https://dmoj.ca/problem/ccc16s4

Interval DP
- Can combine equal adjacent: [1, 1] -> 2
- Can combine [x, y, x]: [5, 7, 5] -> 17
- Goal is to make the largest possible
- Start with smaller intervals first, so we already have their value when using them for larger ones

TC: O(N^3)
"""

from itertools import accumulate

n = int(input())
arr = list(map(int, input().split()))
psa = [0] + list(accumulate(arr))
query = lambda l, r: psa[r + 1] - psa[l]

dp = [[0] * n for _ in range(n)]  # dp[i][j] is whether we can combine all of [i,j] into 1 ball
for i in range(n):
    dp[i][i] = 1

for length in range(1, n):  # start with smaller intervals
    for i in range(n - length):
        j = i + length
        # Find (low,high) where sum[i,low] == sum[high,j], so we can combine all into [i,j]
        # we also need to make sure every interval we are trying to combine can be turned into 1 ball
        # Do this in O(n) using 2 pointers
        low = i
        high = j
        while high > low:  # note: the middle interval may not exist, but we can still combine low and high
            if (query(i, low) == query(high, j) and (low == high - 1 or dp[low + 1][high - 1]) and
                    dp[i][low] and dp[high][j]):
                dp[i][j] = 1
                break
            elif query(i, low) > query(high, j):  # left has greater sum, we need to add more to the right
                high -= 1
            else:  # add more to the left
                low += 1

# get best answer
best = 0
for i in range(n):
    for j in range(n):
        if dp[i][j]:
            best = max(best, query(i, j))
print(best)

# # brute force 3/15 TLE (very easy to understand)
# N = int(input())
# balls = tuple(map(int, input().split()))
#
# sizes = {}
# stack = [balls]
# while stack:
#     current = stack.pop()
#     sizes[current] = max(current)  # remembers max size
#     for i in range(len(current) - 1):
#         if current[i] == current[i + 1]:
#             next = current[:i] + (current[i] + current[i + 1],) + current[i + 2:]
#             if next not in sizes:  # if not already visited
#                 stack.append(next)
#
#     for i in range(len(current) - 2):  # x, x + 2 combining
#         if current[i] == current[i + 2]:
#             next = current[:i] + (current[i] + current[i + 1] + current[i + 2],) + current[i + 3:]
#             if next not in sizes:  # if not already visited
#                 stack.append(next)
#
# max_size = max(sizes.values())
# print(max_size)
