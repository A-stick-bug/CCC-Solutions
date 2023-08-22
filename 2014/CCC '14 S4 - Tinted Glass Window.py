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
    py.add(y1)
    px.add(x2)
    py.add(y2)
    rects.append([x1, y1, x2, y2, t])

px = sorted(list(px))
py = sorted(list(py))
cx = {px[i]: i for i in range(len(px))}  # compressed coordinates
cy = {py[i]: i for i in range(len(py))}

diff = [[0] * (len(px) + 1) for i in range(len(py) + 1)]

for i in range(N):
    x1, y1, x2, y2, t = rects[i]
    x1, y1, x2, y2 = cx[x1], cy[y1], cx[x2], cy[y2]  # use compressed coordinates for difference array
    diff[y1 + 1][x1 + 1] += t
    diff[y2 + 1][x2 + 1] += t
    diff[y1 + 1][x2 + 1] -= t
    diff[y2 + 1][x1 + 1] -= t

res = 0
for i in range(1, len(py)):
    for j in range(1, len(px)):
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        if diff[i][j] >= T:
            res += (py[i] - py[i - 1]) * (px[j] - px[j - 1])  # use the real coordinates when adding tint

print(res)
