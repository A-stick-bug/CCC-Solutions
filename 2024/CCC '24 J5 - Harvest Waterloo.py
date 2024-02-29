# template flood filling question

N = int(input())
M = int(input())
grid = [input() for _ in range(N)]

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

start_r = int(input())
start_c = int(input())
stack = [(start_r, start_c)]
vis = [[False] * M for _ in range(N)]

total = 0
gain = {"S": 1, "M": 5, "L": 10}

vis[start_r][start_c] = True
total += gain[grid[start_r][start_c]]

while stack:
    r, c = stack.pop()
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != "*" and not vis[nr][nc]:
            vis[nr][nc] = True
            total += gain[grid[nr][nc]]
            stack.append((nr, nc))

print(total)
