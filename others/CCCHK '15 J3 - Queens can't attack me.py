def mark_cells(row, col):
    # N is the amount of rows on the board
    directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
    for dr, dc in directions:
        r, c = row, col
        while N > r >= 0 and N > c >= 0:
            grid[r][c] = True
            r += dr
            c += dc


N, M = map(int, input().split())
grid = [[False] * N for _ in range(N)]
for i in range(M):
    r, c = map(int, input().split())
    mark_cells(r - 1, c - 1)

print(sum([i.count(False) for i in grid]))
