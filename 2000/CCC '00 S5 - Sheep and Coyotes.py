# https://dmoj.ca/problem/ccc00s5
# Consider the Voronoi diagram of the points, find the regions that touch the x-axis
# - for each point, keep track of the contiguous interval on the x-axis that is closest to it
# - update this interval by checking the perpendicular bisector between the current and every other point
#
# TC: O(n^2)

inf = 1 << 30


def slope(p1, p2):  # todo: use cross multiplication to compare slopes
    dy = (p2[1] - p1[1])
    dx = (p2[0] - p1[0])
    if dx == 0:  # temporary fix, assumes duplicate points have slope -inf between them
        return inf if dy > 0 else -inf
    return dy / dx


n = int(input())
arr = []
for _ in range(n):
    x = round(float(input()) * 100)
    y = round(float(input()) * 100)
    arr.append((x, y))

# print(arr)

interval = [[0, 100 * 1000] for _ in range(n)]

for i in range(n):  # all pairs comparison
    x1, y1 = arr[i]
    for j in range(n):
        x2, y2 = arr[j]
        if x1 == x2 and y1 == y2:  # same point, ignore
            continue

        m = slope((x1, y1), (x2, y2))

        if m == inf or m == -inf:  # special case: one is directly above the other
            if y1 > y2:
                interval[i][1] = -1  # invalidate interval
            continue

        if m == 0:  # equal y coordinate, use midpoint of x coordinates
            x_int = (x1 + x2) / 2
        else:  # find bisector intersection with x-axis
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            m2 = -1 / m
            b = mid_y - m2 * mid_x  # mid_y = m2*mid_x + b
            x_int = -b / m2  # 0 = m2 * x + b

        if x1 < x2:
            interval[i][1] = min(interval[i][1], x_int)
        else:
            interval[i][0] = max(interval[i][0], x_int)

for i, (x, y) in enumerate(arr):
    # print(interval[i])
    if interval[i][1] >= interval[i][0]:  # non negative range
        print(f"The sheep at ({x / 100:.2f}, {y / 100:.2f}) might be eaten.")

# # Accurate version using Fraction, note that this TLE due to large constant factors
# from fractions import Fraction
#
# inf = 1 << 30
#
#
# def slope(p1, p2):  # todo: use cross multiplication to compare slopes
#     dy = (p2[1] - p1[1])
#     dx = (p2[0] - p1[0])
#     if dx == 0:  # temporary fix, assumes duplicate points have slope -inf between them
#         return inf if dy > 0 else -inf
#     return Fraction(dy, dx)
#
#
# n = int(input())
# arr = []
# for _ in range(n):
#     x = round(float(input()) * 100)
#     y = round(float(input()) * 100)
#     arr.append((x, y))
#
# # print(arr)
#
# interval = [[0, 100 * 1000] for _ in range(n)]
#
# for i in range(n):  # all pairs comparison
#     x1, y1 = arr[i]
#     for j in range(n):
#         x2, y2 = arr[j]
#         if x1 == x2 and y1 == y2:
#             continue
#
#         m = slope((x1, y1), (x2, y2))
#
#         if m == inf or m == -inf:  # special case
#             if y1 > y2:
#                 interval[i][1] = -1  # invalidate interval
#             continue
#
#         if m == 0:
#             x_int = Fraction(x1 + x2, 2)
#         else:
#             mid_x, mid_y = Fraction(x1 + x2, 2), Fraction(y1 + y2, 2)
#             m2 = -Fraction(1, m)
#             b = mid_y - m2 * mid_x  # mid_y = m2*mid_x + b
#             x_int = Fraction(-b, m2)  # 0 = m2 * x + b
#
#         if x1 < x2:
#             interval[i][1] = min(interval[i][1], x_int)
#         else:
#             interval[i][0] = max(interval[i][0], x_int)
#
#
# for i, (x, y) in enumerate(arr):
#     # print(interval[i])
#     if interval[i][1] >= interval[i][0]:  # non negative range
#         print(f"The sheep at ({x / 100:.2f}, {y / 100:.2f}) might be eaten.")
