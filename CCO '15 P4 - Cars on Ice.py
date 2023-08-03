# 6/10 test cases, TLE
# use topo sort (too slow)
# the in-degree is how many cars block the current one

from collections import deque
import sys

input = sys.stdin.readline

n_rows, n_cols = map(int, input().split())
board = [list(input()) for _ in range(n_rows)]
directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

in_degree = [[0] * n_cols for _ in range(n_rows)]  # how many cars are in the way
graph = [[[] for _ in range(n_cols)] for _ in range(n_rows)]  # 'i' has a list of all the cars a cell is blocking

for i in range(n_rows):
    for j in range(n_cols):
        if board[i][j] in directions:
            r, c = i, j
            dr, dc = directions[board[i][j]]
            r += dr
            c += dc
            while 0 <= r < n_rows and 0 <= c < n_cols:
                if board[r][c] != ".":
                    in_degree[i][j] += 1
                    graph[r][c].append((i, j))
                r += dr
                c += dc

q = deque()  # find an in-degree 0
for i in range(n_rows):
    for j in range(n_cols):
        if board[i][j] in directions and in_degree[i][j] == 0:
            q.append((i, j))

while q:
    row, col = q.popleft()
    print(f"({row},{col})")
    for r, c in graph[row][col]:
        in_degree[r][c] -= 1
        if in_degree[r][c] == 0:
            q.append((r, c))
