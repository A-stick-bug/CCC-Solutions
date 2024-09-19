# https://dmoj.ca/problem/ccc06s4
# If you understand basic group theory, the problem becomes just implementation

import sys


def solve():
    n = int(input())
    if n == 0:
        sys.exit()
    arr = [-1] + [[-1] + list(map(int, input().split())) for _ in range(n)]  # 1-indexed

    # check associativity
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if arr[x][arr[y][z]] != arr[arr[x][y]][z]:
                    print("no")
                    return

    # find identity
    identity = -1
    for i in range(1, n + 1):
        if all(arr[i][x] == arr[x][i] == x for x in range(1, n + 1)):
            identity = i
            break
    if identity == -1:  # no identity
        print("no")
        return

    # use identity to find inverse
    for x in range(1, n + 1):
        if not any(arr[x][x_inv] == arr[x_inv][x] == identity for x_inv in range(1, n + 1)):
            print("no")
            return

    print("yes")


while True:
    solve()
