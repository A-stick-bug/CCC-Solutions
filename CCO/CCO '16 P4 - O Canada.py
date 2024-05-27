"""
https://dmoj.ca/problem/cco16p4
harder version of https://dmoj.ca/problem/cco07p2
Q: given a bunch of grids that you can do moves on, check how many pairs
   of equal grids there are after applying moves

- To find equal pairs, we can use the 2-sum method
- We want to apply a 'standard' set of moves to every grid so that equal grids
  have the same form
- if we loop top to bottom, left to right, and flip a 2x2 square every time we encounter
  a marked cell, everything except the last row and column will be un-marked
- we can use bitmask to represent the last row and column to save memory
  (apparently not, there's not enough states, you can just use a set)
"""

N = int(input())
G = int(input())

pairs = 0
seen = [False] * (1 << (2 * N - 1))
for _ in range(G):
    grid = [list(map(lambda x: x == "R", input())) for _ in range(N)]

    # standardize grid by flipping a 2x2 square when we encounter a marked cell
    for i in range(N - 1):
        for j in range(N - 1):
            if grid[i][j]:
                grid[i][j] ^= 1
                grid[i + 1][j] ^= 1
                grid[i][j + 1] ^= 1
                grid[i + 1][j + 1] ^= 1

    state = 0  # turn state into a bitmask to save space
    for j in range(N):  # last row
        if grid[-1][j]:
            state |= 1 << j
    for i in range(N - 1):  # last col
        if grid[i][-1]:
            state |= 1 << (N + i)

    pairs += seen[state]  # 2-sum to match pairs
    seen[state] += 1

print(pairs)
