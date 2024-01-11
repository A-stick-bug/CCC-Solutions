# First fill obvious cases: in a row/column, there is 1 unknown
# Then try to randomly fill in values until you get a working board

from random import randint


# check if the current grid is valid
def is_correct(ans):
    if count_x(ans) != 0:  # make sure it is filled
        return False

    for i in range(3):
        for j in range(3):
            if grid[i][j] != "X" and grid[i][j] != ans[i][j]:  # make sure we didn't modify the original board
                return False

    return all([row[1] - row[0] == row[2] - row[1] for row in ans]) \
        and all([col[1] - col[0] == col[2] - col[1] for col in rotate(ans)])  # check for arithmetic sequences


def fill_certain():
    """main function for solving the grid, fills all ROWS with 1 unknown"""
    for i in range(3):
        if res[i].count("X") == 1:
            pos = res[i].index("X")
            if pos == 0:  # basic math of arithmetic sequences
                res[i][0] = res[i][1] - (res[i][2] - res[i][1])
            elif pos == 2:
                res[i][2] = res[i][1] + (res[i][1] - res[i][0])
            else:
                res[i][1] = (res[i][0] + res[i][2]) // 2


def fill_all():  # tries to fill everything
    global res
    for _ in range(3):  # there are 3 rows/columns total which is how many times we must fill at most
        fill_certain()
        res = rotate(res)  # rotate to do columns
        fill_certain()
        res = rotate(res)  # rotate it back


# small utility functions to clean up code
count_x = lambda grid: sum([row.count("X") for row in grid])  # total number of 'X' in board
rotate = lambda grid: list(map(list, list(zip(*grid))))  # columns <-> rows, is its own inverse
deepcopy = lambda x: [i.copy() for i in x]

grid = [input().split() for _ in range(3)]  # take input
for i in range(3):
    for j in range(3):
        if grid[i][j] != "X":
            grid[i][j] = int(grid[i][j])

res = [i.copy() for i in grid]  # make a copy since we might need to compare to our original grid
fill_all()  # fill trivial cases

# start generating random stuff and hope it works
restore = deepcopy(res)
while not is_correct(res):
    res = deepcopy(restore)  # didn't work, reset state
    for i in range(3):  # try to fill unknown states
        for j in range(3):
            if res[i][j] != 'X':
                continue
            res[i][j] = randint(-1000, 1000)
            fill_all()

assert is_correct(res)  # for testing purposes, makes sure the answer is correct
for r in res:
    print(*r)
