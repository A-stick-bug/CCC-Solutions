# the grid is quite small, so we can use recursive DFS + memoization

import sys

input = sys.stdin.readline
inf = 1 << 30


def solve(r, c, dir):
    if (r, c, dir) in cache:
        return cache[(r, c, dir)]

    if not (0 <= r < ROWS and 0 <= c < COLS):  # out of bounds
        return -inf

    elif r == ROWS - 1 and c == COLS - 1:  # reached destination
        best = 0

    elif dir == "up":  # going up, we can keep going up or turn right
        best = max(solve(r - 1, c, "up"),
                   solve(r, c + 1, "right"))

    elif dir == "down":  # going down, we can keep going down or turn right
        best = max(solve(r + 1, c, "down"),
                   solve(r, c + 1, "right"))

    else:  # just turned, we can continue right, go up, or go down
        best = max(solve(r, c + 1, "right"),
                   solve(r - 1, c, "up"),
                   solve(r + 1, c, "down"))

    cache[(r, c, dir)] = best + graph[r][c]
    return cache[(r, c, dir)]


while True:
    ROWS, COLS = map(int, input().split())
    if ROWS == 0:  # end of input
        break

    graph = [list(input().strip()) for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if graph[i][j] == ".":
                graph[i][j] = 0
            elif graph[i][j] == "*":
                graph[i][j] = -inf
            else:
                graph[i][j] = int(graph[i][j])

    cache = {}
    print(solve(ROWS - 1, 0, "up"))
