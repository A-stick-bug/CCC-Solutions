# MLE, CHECK C++ CODE
# https://dmoj.ca/problem/cco05p5
# On each layer, either (go to right and then go to left) or (go to left and then go to right)
#
# TC: O(n), since there are only 2n possible states

from functools import cache

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]


@cache
def solve(i, loc):
    if i == n:
        return n - loc  # distance to walk to corner
    l, r = arr[i]
    return min(abs(loc - l) + (r - l) + solve(i + 1, r),
               abs(r - loc) + (r - l) + solve(i + 1, l))

print(solve(0, 1) + n - 1)  # add time to drop down levels
