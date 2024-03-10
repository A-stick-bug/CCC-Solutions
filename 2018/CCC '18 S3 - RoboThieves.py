"""
https://dmoj.ca/problem/ccc18s3

BFS with A LOT of implementation

Notes:
- first mark all cells visible by cameras (when we are on a conveyor, they are automatically ignored)
  - if the starting cell is visible by a camera, don't run bfs and automatically print -1 for everything
- now do bfs
  - no need to check for bounds since the map is surrounded by walls
  - if we are on a conveyor, we have to follow it all the way through, note that you don't
    take any steps on the conveyor
"""

from collections import deque


def handle_camera(r, c):
    """mark every cell visible by this camera"""
    for dr, dc in dir4:
        nr, nc = r, c
        while grid[nr][nc] != "W":
            if grid[nr][nc] not in conveyor:
                camera[nr][nc] = True
            nr += dr
            nc += dc


def follow_conveyor(r, c):
    while grid[r][c] in conveyor:
        if dist[r][c] == -2:  # cycle in conveyor: just return te location of a wall
            return 0, 0
        dist[r][c] = -2  # placeholder value to prevent revisiting this cell
        dr, dc = conveyor[grid[r][c]]
        r += dr
        c += dc
    return r, c


N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
camera = [[False] * M for _ in range(N)]

dir4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]
conveyor = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

for i in range(N):  # mark cells visible by camera
    for j in range(M):
        if grid[i][j] == "C":
            handle_camera(i, j)

q = deque()
dist = [[-1] * M for _ in range(N)]
for i in range(N):  # find starting location
    for j in range(M):
        if grid[i][j] == "S" and not camera[i][j]:
            q.append((i, j))
            dist[i][j] = 0

while q:  # run bfs while handling conveyors
    r, c = q.popleft()
    for dr, dc in dir4:
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == "W" or camera[nr][nc] or dist[nr][nc] != -1:  # marked by camera or already visited
            continue

        if grid[nr][nc] in conveyor:  # move onto conveyor, follow it through
            nr, nc = follow_conveyor(nr, nc)
            if grid[nr][nc] == "W" or camera[nr][nc] or dist[nr][nc] != -1:  # end location of conveyor is invalid
                continue

        dist[nr][nc] = dist[r][c] + 1  # update distances of adjacent cell
        q.append((nr, nc))

for i in range(N):  # print answers
    for j in range(M):
        if grid[i][j] == ".":
            print(dist[i][j])
