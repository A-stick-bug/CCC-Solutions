# time-consuming question, and lots of case work

# let x be the number of unknown numbers

# subtask 1
# if x <= 3, we can just use loops and keep on filling rows with only 1 'X' until we get the answer

# subtask 3
# if x >= 8 (at most 1 known number), we can use the same number
# if x == 7, slightly more complicated, 2 cases: same row or different row

# all subtasks (4-6 X)
# for many possible placements of X, we can just use the fill_certain function up to 6 times to get an answer
# if we can't get an answer from using fill_certain, we just brute force possible values with backtracking

import sys


# check if the current grid is valid
def is_correct(ans):
    if count_x(ans) != 0:
        return False

    for i in range(3):
        for j in range(3):
            if grid[i][j] != "X" and grid[i][j] != ans[i][j]:
                return False

    return all([row[1] - row[0] == row[2] - row[1] for row in ans]) \
        and all([col[1] - col[0] == col[2] - col[1] for col in rotate(ans)])


# main function for solving the grid
def fill_certain():  # for filling rows with only 1 unknown
    for i in range(3):
        if res[i].count("X") == 1:
            pos = res[i].index("X")
            if pos == 0:
                res[i][0] = res[i][1] - (res[i][2] - res[i][1])
            elif pos == 2:
                res[i][2] = res[i][1] + (res[i][1] - res[i][0])
            else:
                res[i][1] = (res[i][0] + res[i][2]) // 2


def get_n():
    x = []
    for i in range(3):
        for j in range(3):
            if res[i][j] != "X":
                x.append((i, j))
    return x


count_x = lambda grid: sum([row.count("X") for row in grid])  # total number of 'X' in input
rotate = lambda grid: list(map(list, list(zip(*grid))))  # make the columns rows (90 degrees rotate)

grid = [input().split() for _ in range(3)]
for i in range(3):
    for j in range(3):
        if grid[i][j] != "X":
            grid[i][j] = int(grid[i][j])
res = [i.copy() for i in grid]

x = count_x(grid)
if x < 7:
    for _ in range(6):  # there are 6 rows/columns total which is how many times we must fill at most
        fill_certain()
        res = rotate(res)  # rotate to do columns
        fill_certain()
        res = rotate(res)  # rotate it back

elif x >= 8:  # use same number (d = 0)
    a = 1  # placeholder
    for row in grid:
        for num in row:
            if num != "X":
                a = num
    res = [[a] * 3 for _ in range(3)]

elif x == 7:  # 2 empty
    rotated = False  # for only 2 empty, we can make all rows the same (rotate if one row as both numbers)
    if any([row.count("X") < 2 for row in grid]):
        res = rotate(res)
        rotated = True
    x1, x2 = get_n()
    r1, c1 = x1
    r2, c2 = x2
    res[r1] = [res[r1][c1]] * 3
    res[r2] = [res[r2][c2]] * 3

    # let the function handle the rest as there will only be one unknown row
    res = rotate(res)
    fill_certain()
    res = rotate(res)

    if rotated:
        res = rotate(res)

elif not is_correct(res):  # not filled yet, start brute forcing
    ...

assert is_correct(res)
for r in res:
    print(*r)
