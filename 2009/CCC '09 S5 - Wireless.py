# MLE on last three cases, the c++ solution is the exact same but passes because c++ is faster
# I would recommend checking out 2008 S2 first if you haven't
# using difference arrays for O(n) range update

from math import floor

ROWS = int(input())
COLS = int(input())
k = int(input())
dist = lambda x, r: floor((r ** 2 - x ** 2) ** 0.5)
diff = [[0] * (COLS + 1) for _ in range(ROWS)]  # difference array, +1 on columns to prevent going out of bounds

for _ in range(k):
    col, row, radius, rate = map(int, input().split())
    col -= 1  # turn into 0-indexing
    row -= 1

    for i in range(max(0, row - radius), min(ROWS - 1, row + radius) + 1):  # make sure we stay in range
        r_dist = abs(i - row)  # up-down distance
        width = dist(r_dist, radius)

        start = max(0, col - width)
        end = min(COLS - 1, col + width)
        diff[i][start] += rate
        diff[i][end + 1] -= rate

cur = greatest = occurrences = 0

for i in range(ROWS):
    for j in range(COLS + 1):
        cur += diff[i][j]
        if cur > greatest:
            greatest = cur
            occurrences = 1
        elif cur == greatest:
            occurrences += 1

print(greatest)
print(occurrences)
