# https://dmoj.ca/problem/ccc25j5
# dp with memory optimization, only store 1 row at a time
# use padding to prevent transitions from out of bounds
#
# TC: O(RC), time limit is quite lenient

R = int(input())
C = int(input())
M = int(input())

val = 1
row1 = [0] * (C + 1)
row2 = [0] * (C + 1)
row1[-1] = row2[-1] = 1 << 30  # infinity

for _ in range(1, R + 1):
    arr = [0] * (C + 1)
    for j in range(C):
        arr[j] = val
        val += 1
        if val == M + 1:
            val = 1
    for i in range(C):
        row2[i] = min(row1[i - 1], row1[i], row1[i + 1]) + arr[i]

    row1 = row2
    row2 = [0] * (C + 1)
    row2[-1] = 1 << 30

print(min(row1))
