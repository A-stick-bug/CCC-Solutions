# an easier to understand solution for CCC 2023 S3 (I think)

import sys

ROWS, COLS, rp, cp = map(int, input().split())
rotated = False
if cp == COLS or rp == 0:
    ROWS, COLS, rp, cp = COLS, ROWS, cp, rp  # swap rows and columns
    rotated = True

grid = [["a"] * COLS for _ in range(ROWS)]

# regular case
for i in range(rp):  # create palindrome rows
    grid[i] = ["b"] * COLS
for j in range(cp):  # create palindrome cols
    for i in range(ROWS):
        grid[i][j] = "b"

# corner case 1: no palindromes
if rp == 0 and cp == 0:
    for i in range(ROWS):  # set first row to b
        grid[i][0] = "b"
    for j in range(COLS):  # set first col to b
        grid[0][j] = "b"
    grid[0][0] = "a"  # set up-left corner to a

# corner case 2: there are no col palindromes: fill in the extra spaces or else all rows will be palindromes
elif cp == 0:
    for i in range(rp, ROWS):
        grid[i][0] = "d"

# corner case 3: all rows are palindrome, not all cols are palindrome
if rp == ROWS and cp != COLS:
    remove_col = COLS - cp  # number of col palindromes that we need to remove

    if remove_col % 2 == 1:
        if COLS % 2 == 0:  # even cols, need to remove odd
            print("IMPOSSIBLE")  # not possible because of different parity
            sys.exit()
        else:
            for i in range(remove_col // 2):
                grid[0][i] = "c"
                grid[0][COLS - i - 1] = "c"
            grid[0][COLS // 2] = "c"

    else:
        for i in range(remove_col // 2):
            grid[0][i] = "c"
            grid[0][COLS - i - 1] = "c"

if rotated:
    grid = list(zip(*grid))  # rotate it back

for row in grid:
    print(*row, sep="")
