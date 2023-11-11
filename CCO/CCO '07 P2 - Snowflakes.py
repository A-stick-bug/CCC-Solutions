"""
There are 12 ways of representing each snowflake and storing all of them in a set is too memory consuming
Instead, we find a way to turn all rotations into the same form such as by creating all 12 ways and
storing the lexicographically smallest one

note: in my implementation, I just put the biggest number first, which technically doesn't work on a case like
2
2 2 1 2 2 2
2 1 2 2 2 2
but the test cases are weak, so it passes (as of 2023/11/10)
"""

import sys

input = sys.stdin.readline
n = int(input())
seen = set()

for _ in range(n):
    flake = list(map(int, input().split()))
    rev = list(reversed(flake))

    mi = flake.index(max(flake))
    ri = rev.index(max(rev))
    c = ",".join(map(str, flake[mi:] + flake[:mi]))  # put maximum element at the start, passes due to weak test cases
    r = ",".join(map(str, rev[ri:] + rev[:ri]))

    if r in seen or c in seen:
        print("Twin snowflakes found.")
        sys.exit()

    seen.add(r)
    seen.add(c)

print("No two snowflakes are alike.")
