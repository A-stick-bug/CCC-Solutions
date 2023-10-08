# NO SEGMENT TREE
# 16 difference arrays to handle updates
# sparse table for O(1) range GCD query to check if the array we created is valid

from math import lcm, gcd
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(M)]

# use difference array to handle queries for all gcd values
diff = [[0] * (N + 2) for _ in range(17)]  # 1-indexed + padding at the back
for i, j, x in queries:
    diff[x][i] += 1
    diff[x][j + 1] -= 1

# use lcm to create the output
res = [0] * N
for i in range(1, N + 1):
    cur = 1
    for z in range(17):
        diff[z][i] += diff[z][i - 1]
        if diff[z][i] != 0:  # need to include this gcd as a factor of cur
            cur = lcm(cur, z)
    res[i - 1] = cur

# after creating the array, we have the make sure the GCD for each range is correct
# we can do this quickly using a sparse table
bits = N.bit_length()  # log2
st = [[0] * bits for _ in range(N)]
for i in range(N):
    st[i][0] = res[i]  # column 1: base cases

for k in range(1, bits):
    for i in range(N - (1 << k) + 1):
        st[i][k] = gcd(st[i][k - 1], st[i + (1 << (k - 1))][k - 1])

# check if query GCDs are correct using sparse table
for l, r, x in queries:
    l -= 1  # 0-indexed
    r -= 1
    k = (r - l + 1).bit_length() - 1
    if gcd(st[l][k], st[r - (1 << k) + 1][k]) != x:
        print("Impossible")
        sys.exit()

print(*res)
