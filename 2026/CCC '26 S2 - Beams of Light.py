# https://dmoj.ca/problem/ccc26s2
# Template difference array

import sys
from itertools import accumulate

input = sys.stdin.readline

N = int(input())
L = int(input())
Q = int(input())

dif = [0] * (N + 2)
for _ in range(L):
    idx, s = map(int, input().split())
    l = max(1, idx - s)
    r = min(N, idx + s)
    dif[l] += 1
    dif[r + 1] -= 1
dif = list(accumulate(dif))

for _ in range(Q):
    idx = int(input())
    print("Y" if dif[idx] else "N")
