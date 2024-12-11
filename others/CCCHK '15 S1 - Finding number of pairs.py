# https://dmoj.ca/problem/hkccc15s1
# efficiently finding all pairs that satisfy condition using binary search
# subtract same index cases since `i < j`

from bisect import bisect_left

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

total = 0
for i in range(N):
    x = bisect_left(arr, M - arr[i] + 1)
    if arr[i] * 2 <= M:  # prevent double count
        total -= 1
    total += x

print((total // 2) % (10 ** 9 + 7))
