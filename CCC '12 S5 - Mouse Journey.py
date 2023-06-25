# brute force BFS and DFS didn't work, so I had to use dynamic programming (15/15)

ROWS, COLS = map(int, input().split())
grid = [[True for _ in range(COLS)] for _ in range(ROWS)]

for _ in range(int(input())):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = False  # minus one because the problem uses 1-indexing

dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
dp[0][0] = 1

for row in range(ROWS):
    for col in range(COLS):
        if not grid[row][col]:
            continue
        if row > 0:
            dp[row][col] += dp[row - 1][col]
        if col > 0:
            dp[row][col] += dp[row][col - 1]

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
