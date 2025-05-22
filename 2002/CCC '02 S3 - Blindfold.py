"""
https://dmoj.ca/problem/ccc02s3
Given a sequence of M moves (M ~ RC), find all possible starting cells

Extra implementation part: try all starting directions
Store the traced path as its own grid, efficiently match with the full grid using bitmask

TC: O(1/32 * R^2 * C^2)
Note: Worse case is extremely hard to construct. Average case is closer to O(1/32 * R * C^2)
"""

R = int(input())
C = int(input())
ans = [list(input()) for _ in range(R)]
grid = [0] * R

# compress to bitmask
for i in range(R):
    row = ans[i]
    for j in range(C):
        if row[j] == "X":
            grid[i] |= 1 << j

# trace path
M = int(input())
x, y = 0, 0
dx, dy = (1, 0)
path = [(0, 0)]
for _ in range(M):
    move = input()
    if move == "F":  # move forwards
        x += dx
        y += dy
    elif move == "L":  # rotate 90 deg CCW
        dx, dy = -dy, dx
    else:  # rotate 90 deg CW
        dx, dy = dy, -dx
    path.append((x, y))

# make path coordinates positive to fit in grid
min_x = min(x for x, y in path)
min_y = min(y for x, y in path)
for i, (x, y) in enumerate(path):
    path[i] = (x - min_x, y - min_y)

path_r = max(x for x, y in path) + 1
path_c = max(y for x, y in path) + 1
path_grid = [[0] * path_c for _ in range(path_r)]
for x, y in path:
    path_grid[x][y] = 1
ending_loc = path[-1]


def add_starting_points(path_grid, ending_loc):
    """Check how many subgrids matches and add their end points"""
    pr, pc = len(path_grid), len(path_grid[0])

    # compress to bitmask
    masks = [0] * pr
    for i in range(pr):
        for j in range(pc):
            if path_grid[i][j]:
                masks[i] |= 1 << j

    # match subgrids, (sx,sy) is the top-left corner of subgrid
    ex, ey = ending_loc
    for sx in range(R - pr + 1):
        for sy in range(C - pc + 1):
            works = True
            for r in range(pr):
                if (masks[r] << sy) & grid[sx + r] != 0:  # path collides with obstacle
                    works = False
                    break
            if works:
                ans[ex + sx][ey + sy] = "*"  # mark ending location


for _ in range(4):
    add_starting_points(path_grid, ending_loc)

    ex, ey = ending_loc
    ending_loc = (ey, len(path_grid) - ex - 1)
    path_grid = list(zip(*path_grid[::-1]))  # rotate 90 CW

    # for r in path_grid:
    #    print(r)
    # print("end:", ending_loc)
    # print()

for row in ans:
    print("".join(row))

"""
2
4
....
.XXX
3
F
R
F
"""
