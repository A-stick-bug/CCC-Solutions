from collections import deque


def bfs(grid, ROWS, COLS):
    distances = [[50 for _ in range(COLS)] for _ in range(ROWS)]
    distances[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        row, col = q.popleft()
        if row == ROWS - 1 and col == COLS - 1:  # end reached
            return distances[row][col]

        cell = grid[row][col]
        if cell == "-":
            directions = [(0, 1), (0, -1)]
        elif cell == "|":
            directions = [(1, 0), (-1, 0)]
        else:
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if 0 <= new_r < ROWS and 0 <= new_c < COLS \
                    and grid[new_r][new_c] != "*" and distances[new_r][new_c] == 50:
                distances[new_r][new_c] = distances[row][col] + 1
                q.append((new_r, new_c))
    return -1


for _ in range(int(input())):
    # create graph (or grid)
    ROWS = int(input())
    COLS = int(input())
    graph = []
    for i in range(ROWS):
        graph.append(list(input()))

    print(bfs(graph, ROWS, COLS))

