# https://dmoj.ca/problem/ccc02s5
# - the box is symmetric in both X and Y
# - instead of reflecting the line, simply shift the box
# - if after a large number of iterations, we still didn't hit a corner there is probably a cycle

import sys

MX = int(input())
MY = int(input())

cur_x = int(input())  # current ball location
cur_y = 0

slope = int(input()) / (MX - cur_x)  # equation of line
y_int = -slope * cur_x

for bounce in range(100000):
    x_line = cur_x // MX * MX + MX  # vertical line's x coordinate
    y_line = cur_y // MY * MY + MY
    intersect_x = cur_y + (x_line - cur_x) * slope  # y-value at which line hits `x = x_line`
    intersect_y = cur_x + (y_line - cur_y) * (1 / slope)  # x-value at which line hits `y = y_line`

    if intersect_x < y_line:  # hit vertical `x_line` first
        if y_line - intersect_x < 5 or intersect_x - (y_line - MY) < 5:  # hit corner
            print(bounce)
            sys.exit()
        cur_x = x_line
        cur_y = intersect_x

    else:  # hit horizontal `y_line` first
        if x_line - intersect_y < 5 or intersect_y - (x_line - MX) < 5:  # hit corner
            print(bounce)
            sys.exit()
        cur_x = intersect_y
        cur_y = y_line

print(0)
