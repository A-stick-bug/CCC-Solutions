# weird geometry problem, basically, take any 3 points
# if it has an obtuse angle, the diameter is just the longest side
# otherwise, use nerdy math formula

from math import sqrt

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
res = 0


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# acute triangles
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ix, iy = points[i]
            jx, jy = points[j]
            kx, ky = points[k]

            a = dist(ix, iy, jx, jy)
            b = dist(jx, jy, kx, ky)
            c = dist(ix, iy, kx, ky)
            s = (a + b + c) / 2

            # obtuse
            if (a**2 + b**2 - c**2 < 0) or (b**2 + c**2 - a**2 < 0) or (c**2 + a**2 - b**2 < 0):
                d = max(dist(*points[i], *points[j]), dist(*points[i], *points[k]), dist(*points[k], *points[j]))
            else:  # acute
                d = (a * b * c) / (2 * sqrt(s * (s - a) * (s - b) * (s - c)))

            res = max(res, d)

res = round(res, 2)
print(f"{res:.2f}")  # format to 2 decimal places
