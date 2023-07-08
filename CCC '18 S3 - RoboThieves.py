# 10/15, didn't consider the conveyors

from collections import deque
import sys

ROWS, COLS = map(int, input().split())
graph = [list(input()) for _ in range(ROWS)]
distances = [[10000 for _ in range(COLS)] for _ in range(ROWS)]  # distances to each cell
cameras = [[False for _ in range(COLS)] for _ in range(ROWS)]  # cells that cameras can see
flag = False  # if the starting cell is covered by camera, you cannot go anywhere

# W: wall, S: start, dot: destinations+empty, C: cameras (4 directional)
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()

for r in range(ROWS):
    for c in range(COLS):
        cell = graph[r][c]
        if cell == "C":
            # track cells visible to camera
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                while graph[new_r][new_c] != "W":
                    if graph[new_r][new_c] == ".":
                        cameras[new_r][new_c] = True
                    if graph[new_r][new_c] == "S":
                        flag = True
                    new_r += dr
                    new_c += dc

        if cell == "S":
            q.append((r, c))
            distances[r][c] = 0

while q:
    row, col = q.popleft()
    for dr, dc in directions:
        new_r = row + dr
        new_c = col + dc
        # regular path no conveyor and not caught by camera --- and not cameras[new_r][new_c]
        if graph[new_r][new_c] == "." and not cameras[new_r][new_c] and distances[new_r][new_c] == 10000:
            q.append((new_r, new_c))
            distances[new_r][new_c] = min(distances[new_r][new_c], distances[row][col] + 1)

# from numpy import matrix
# print(matrix(distances))

for r in range(ROWS):
    for c in range(COLS):
        if graph[r][c] == ".":
            print(distances[r][c] if distances[r][c] != 10000 and not flag else -1)

