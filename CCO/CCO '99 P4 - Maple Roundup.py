# https://dmoj.ca/problem/cco99p4
# Standard convex hull
# Note: this problem has duplicate points, the <= in the slope comparison handles this
# TC: O(nlogn)

from fractions import Fraction

inf = 1 << 30


def solve():
    def slope(p1, p2):  # todo: use cross multiplication to compare slopes
        dy = (p2[1] - p1[1])
        dx = (p2[0] - p1[0])
        if dx == 0:  # temporary fix, assumes duplicate points have slope -inf between them
            return inf if dy > 0 else -inf
        return Fraction(dy, dx)

    def dist(p1, p2):
        return ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5

    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]  # (x,y)

    arr.sort()

    # solve upper hull
    hull1 = []  # index of hull points
    for cur in arr:
        while len(hull1) >= 2 and slope(hull1[-2], cur) <= slope(hull1[-1], cur):
            hull1.pop()
        hull1.append(cur)

    # solve lower hull
    hull2 = []
    for cur in arr:
        while len(hull2) >= 2 and slope(hull2[-2], cur) >= slope(hull2[-1], cur):
            hull2.pop()
        hull2.append(cur)

    hull = hull1 + hull2[::-1]

    # print(hull)

    total = sum(dist(hull[i], hull[i - 1]) for i in range(1, len(hull)))

    print(f"{total:.2f}")


t = int(input())
for _ in range(t):
    solve()

"""
5
7
5 5
0 0
3 1
10 0
3 -1
5 -5
0 5
4
0 0
10 0
5 10
5 5
4
2 9
1 0
9 9
6 2
4
0 0
0 1
1 0
1 1
6
0 0
2 1
2 -1
4 1
4 0
4 -1

31.21
32.36
29.06
4.00
10.47

duplicate point example
1
7
0 0
0 1
1 1
1 1
1 2
2 0
2 2

6 + sqrt2 = 7.41
"""
