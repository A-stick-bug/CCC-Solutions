# MLE on last three cases, the c++ solution is the exact same but passes because c++ is faster

# I would recommend checking out 2008 S2 first if you haven't
# using difference arrays for O(n) range update (instead of O(n^2))
# O(1) range update is impossible because for each row, we update a difference range

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

    # for each row, calculate the range we need to update
    for i in range(max(0, row - radius), min(ROWS - 1, row + radius) + 1):  # make sure we stay in range
        r_dist = abs(i - row)  # up-down distance, use this to find width using pythagorean theorem
        width = dist(r_dist, radius)

        # update difference array using width and the circle's center
        start = max(0, col - width)  # don't go out of bounds
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
