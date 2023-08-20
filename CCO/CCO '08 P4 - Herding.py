# O(mn)
# since the questions guarantees that the cats will stay inside, we just have to find how many cycles there are
# similar to the method used in CCC 2018 S3
# for each cell, follow its path until it forms a cycle with itself or joins with another path


def bfs(row, col):
    path = set()  # current path
    while True:
        state = grid[row][col]

        if (row, col) in path:  # cycle detected
            for r, c in path:
                grid[r][c] = "."  # mark these as visited
            return True

        elif state == ".":  # current path joins another, no cage is needed
            for r, c in path:
                grid[r][c] = "."
            return False  # no extra cage needed

        path.add((row, col))
        dr, dc = dir[state]  # go to next cell in the path
        row += dr
        col += dc


dir = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
ROWS, COLS = map(int, input().split())
grid = [list(input()) for _ in range(ROWS)]
res = 0

for i in range(ROWS):
    for j in range(COLS):
        res += bfs(i, j)

print(res)
