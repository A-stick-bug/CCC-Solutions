# Using 2D difference array/PSA plus coordinate compression (coordinates go up to a billion)
# O(n^2) where n is the number of glass (technically the number of unique x and y coordinates for the difference array)

from sys import stdin

input = stdin.readline

N = int(input())
T = int(input())
px = set()  # set of points
py = set()
rects = []

for i in range(N):
    x1, y1, x2, y2, t = map(int, input().split())
    px.add(x1)
    px.add(x2)
    py.add(y1)
    py.add(y2)
    rects.append([x1, y1, x2, y2, t])

px = sorted(list(px))
py = sorted(list(py))
cx = {px[i - 1]: i for i in range(1, len(px) + 1)}  # compressed coordinates
cy = {py[i - 1]: i for i in range(1, len(py) + 1)}

diff = [[0] * (len(px) + 1) for i in range(len(py) + 1)]

for i in range(N):
    x1, y1, x2, y2, t = rects[i]
    x1, y1, x2, y2 = cx[x1], cy[y1], cx[x2], cy[y2]  # use compressed coordinates for difference array
    diff[y1][x1] += t
    diff[y2][x2] += t
    diff[y1][x2] -= t
    diff[y2][x1] -= t

res = 0
for i in range(1, len(py) + 1):
    for j in range(1, len(px) + 1):  # convert back into regular array
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        if diff[i][j] >= T:
            # height * width for total area of this compressed region
            res += (py[i] - py[i - 1]) * (px[j] - px[j - 1])  # use the real coordinates when adding tint

print(res)
