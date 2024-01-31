# https://dmoj.ca/problem/ccoqr16p3
# mostly just implementation and a bit of math
# the key is noticing you can compute the gaps between 2 points (on the x-axis) in O(1) using math

import sys

input = sys.stdin.readline
range_sum = lambda l, r: (r - l + 1) * (l + r) // 2  # get the sum of [l, l+1, l+2, ..., r-1, r]

N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(M)]
points.sort(key=lambda x: x[1])  # sort by column number for line sweep
points.append((0, N + 1))   # extra point to avoid missing the values at the end

prev_r = prev_c = 0
total = 0
for r, c in points:
    r = N - r + 1  # reflect for convenience
    diff_c = c - prev_c  # distance (in x) between this and previous point
    total += range_sum(max(0, prev_r - diff_c + 1), prev_r)

    prev_r = max(r, prev_r - diff_c)
    prev_c = c

print(total)
