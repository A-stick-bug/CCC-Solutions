# 9/15, check C++ code for full solution
# longest decreasing path: brute force dfs + memoization
# TC: O(N^3), total of N^2 states with O(N) transitions

from functools import cache

n = int(input())
points = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

dist = lambda a, b: (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])


@cache
def solve(cur, md):
    best = 0
    for adj in range(1, n + 1):
        d = dist(points[cur], points[adj])
        if md > d:
            best = max(best, 1 + solve(adj, d))
    return best


print(solve(0, 1 << 60) - 1)  # -1 because at the end, we end up going to the same node twice
