# O(n*log(n)), sorting, binary search, dictionaries, and simple combinatorics

from bisect import bisect_left
from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())

rows = defaultdict(list)  # rows[r] has every column that has a point on r
cols = defaultdict(list)
points = []

for _ in range(n):
    r, c = map(int, input().split())
    rows[r].append(c)
    cols[c].append(r)
    points.append((r, c))

for key in rows:  # sort all points
    rows[key].sort()
for key in cols:
    cols[key].sort()

# print(rows)
# print(cols)

total = 0
for r, c in points:
    ri = bisect_left(rows[r], c)
    ci = bisect_left(cols[c], r)
    # treat (r,c) as the center, find the number of points up, down, left, and right
    total += (ri * ci * (len(rows[r]) - ri - 1) * (len(cols[c]) - ci - 1))

print(total * 2)  # x2 because there are 2 ways to make bow ties from a set of 5 valid points
