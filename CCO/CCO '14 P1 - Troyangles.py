# Probably the only solution out here that doesn't iterate the grid in reverse
# O(n^2*log(n))
# Dynamic programming (DP) approach
# We can use a prefix sum array (PSA) + binary search to see how big we can make our triangle at each cell (i,j)

from itertools import accumulate
import sys

input = sys.stdin.readline
n = int(input())
grid = [list(map(lambda x: 0 if x == "." else 1, list(input().strip()))) for _ in range(n)]

psa = list(map(lambda x: [0] + list(accumulate(x)), grid))  # make a PSA for each row
query = lambda arr, l, r: arr[r + 1] - arr[l]


def find_size(i, j):
    """get the maximum possible size triangle we can make on row i, centered around j"""
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if j - mid >= 0 and j + mid < n and query(psa[i], j - mid, j + mid) == mid * 2 + 1:  # works
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


total = sum(grid[0])
prev = grid[0]

for i in range(1, n):
    cur = grid[i].copy()
    for j in range(1, n - 1):
        if prev[j] == 0:  # no triangles here
            continue

        size = find_size(i, j)  # max size possible triangle centered around the current cell
        cur[j] = min(prev[j], size) + 1  # triangle size may be limited by previous layers

    prev = cur.copy()
    total += sum(cur)

print(total)
