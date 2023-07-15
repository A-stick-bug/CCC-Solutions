# FIRST AD HOC CONSTRUCTIVE

from math import ceil


def palindrome(rows, cols, rp, cp):
    if rp == rows and cp == cols:  # corner case: all palindromes
        return [["a" for _ in range(cols)] for _ in range(rows)]

    flipped = False
    if cp == cols or rp == 0:  # rotate grid
        grid = [["a" for _ in range(rows)] for _ in range(cols)]
        rows, cols = cols, rows
        rp, cp = cp, rp
        flipped = True
    else:
        grid = [["a" for _ in range(cols)] for _ in range(rows)]

    if rp == 0 and cp == 0:  # corner case: no palindromes
        for col in range(cols):
            grid[0][col] = "b"
        for row in range(rows):
            grid[row][0] = "b"
        grid[0][0] = "z"
        if flipped:
            grid = list(zip(*grid))  # rotate it back
        return grid

    # generating palindromes: for regular test cases
    for i in range(rp):
        for j in range(cols):
            grid[i][j] = "b"
    for j in range(cp):
        for i in range(rows):
            grid[i][j] = "b"

    if cp == 0:
        for i in range(rp, rows):
            grid[i][0] = "c"

    if rp == rows:
        if cp == 0:
            for i in range(cols):
                grid[0][i] = "c"

        elif cp % 2 == cols % 2:  # same parity on even
            for i in range(ceil((cols - cp) / 2)):
                grid[0][i] = "c"
                grid[0][cols - i - 1] = "c"

        elif cols % 2 == 0 and (cols - cp) % 2 == 1:  # different parity on even = impossible
            return "IMPOSSIBLE"

        else:  # different parity but it's fine because odd number of columns (just use the middle column)
            start = end = cols // 2  # middle of array
            i = 0
            repeats = ceil((cols - cp) / 2)
            while i < repeats:  # start removing palindromes from middle
                grid[0][start] = "c"
                grid[0][end] = "c"
                start -= 1
                end += 1
                i += 1

    if flipped:
        grid = list(zip(*grid))  # rotate it back
    return grid


x = list(map(int, input().split()))

output = palindrome(*x)
for i in output:
    if output == "IMPOSSIBLE":
        print(output)
        break
    else:
        print("".join(i))

# this code below helped me come up with the solution faster
# testing if the correct answer is output

# def count_palindromes(grid):
#     grid = list(grid)
#     r = c = 0
#     for i in grid:
#         if i == i[::-1]:
#             r += 1
#     grid = zip(*grid)
#     for i in grid:
#         if i == i[::-1]:
#             c += 1
#     return r, c

# looking for bugs in my code
from random import randint
# x = list(map(int, input().split()))
# from random import randint
#
# for i in range(100):
#     x = [2,0,0,0]
#     x[1] = randint(2,10)
#     x[2] = randint(0,x[0])
#     x[3] = randint(0,x[1])
#
#     # print(x)
#     output = palindrome(*x)
#     # for i in output:
#     #     if output == "IMPOSSIBLE":
#     #         print(output)
#     #         break
#     #     else:
#     #         print("".join(i))
#
#     if output != "IMPOSSIBLE":
#         r,c = count_palindromes(output)
#         if r != x[2] or c != x[3]:
#             print(x)
#             print(r,c)
