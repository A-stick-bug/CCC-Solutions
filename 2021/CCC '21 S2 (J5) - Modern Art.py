# using a hash table
# queries are 1-indexed so we minus 1

R = int(input())
C = int(input())

rows = [False] * R  # False: Black, True: Gold
cols = [False] * C

queries = int(input())
for _ in range(queries):
    t, i = input().split()
    if t == "R":
        rows[int(i) - 1] = not rows[int(i) - 1]  # B --> G or G --> B
    else:
        cols[int(i) - 1] = not cols[int(i) - 1]

grid = [[False] * C for _ in range(R)]  # create the actual grid based on what rows/cols were flipped
for r in range(R):
    if rows[r]:
        grid[r] = [True] * C
for c in range(C):
    if cols[c]:
        for r in range(R):
            grid[r][c] = not grid[r][c]

print(sum(sum(row) for row in grid))
