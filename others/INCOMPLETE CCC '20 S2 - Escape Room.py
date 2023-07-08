# 13/15 TLE, using BFS

from collections import deque


def find_pairs(num):
    pairs = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            pairs.append((i, num // i))
            if i != num // i:
                pairs.append((num // i, i))
    return pairs


ROWS = int(input())
COLS = int(input())
grid = []
for i in range(ROWS):
    grid.append(list(map(int, input().split())))

queue = deque()
queue.append((1,1))
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
no = True

while queue:
    cell = queue.popleft()
    row = cell[0]
    col = cell[1]
    visited[row-1][col-1] = True
    if row == ROWS and col == COLS:
        print("yes")
        no = False
        break

    pairs = find_pairs(grid[row-1][col-1])
    for i, j in pairs:
        if 0 <= i-1 < ROWS and 0 <= j-1 < COLS and not visited[i-1][j-1]:
            queue.append((i,j))

if no: print("no")
