"""
15/15
Very easy for a dynamic programming problem (and for a S5)

Explanation of code:
- each cell represents the number of possible path to get there
- added an extra row and column of 0 to prevent index error (and because there are 0 possible path to get there)
- all cells with cats will stay 0 (can't go there)

Dynamic programming part:
- the possible ways to get to a cell is the sum of the possible ways to get to the cell on top and to the left

Example: State of dp after processing all cells for ROWS = 3, COLS = 3, CATS = 0
1 1 1
1 2 3
1 3 6
"""

ROWS, COLS = map(int, input().split())

# extra array to track cats for simplicity
cats = [[False for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
for i in range(int(input())):  # cats
    r, c = map(int, input().split())
    cats[r][c] = True

# add extra row and col to prevent array out of bounds
dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
dp[1][1] = 1

for r in range(1, ROWS + 1):
    for c in range(1, COLS + 1):
        if not cats[r][c]:
            dp[r][c] += dp[r-1][c] + dp[r][c-1]

print(dp[-1][-1])


# brute force BFS, MLE
# no path will be repeated because you can only move right and down

# from collections import deque
#
# ROWS, COLS = map(int, input().split())
# end = (ROWS - 1, COLS - 1)
# grid = [[True for _ in range(COLS)] for _ in range(ROWS)]
#
# for _ in range(int(input())):
#     r, c = map(int, input().split())
#     grid[r - 1][c - 1] = False
#
# paths = 0
# directions = [(1, 0), (0, 1)]
# q = deque()
# q.append((0, 0))
# while q:
#     row, col = q.popleft()
#     if (row, col) == end:
#         paths += 1
#         continue
#     for dr, dc in directions:
#         new_r, new_c = row + dr, col + dc
#         if new_r < ROWS and new_c < COLS and grid[new_r][new_c]:
#             q.append((new_r, new_c))
#
# print(paths)


# brute force DFS, TLE
# ROWS, COLS = map(int, input().split())
# end = (ROWS - 1, COLS - 1)
# grid = [[True for _ in range(COLS)] for _ in range(ROWS)]
#
# for _ in range(int(input())):
#     r, c = map(int, input().split())
#     grid[r - 1][c - 1] = False
#
# paths = 0
# directions = [(1, 0), (0, 1)]
# stack = [(0,0)]
# while stack:
#     row, col = stack.pop()
#     if (row, col) == end:
#         paths += 1
#         continue
#     for dr, dc in directions:
#         new_r, new_c = row + dr, col + dc
#         if new_r < ROWS and new_c < COLS and grid[new_r][new_c]:
#             stack.append((new_r, new_c))
#
# print(paths)
