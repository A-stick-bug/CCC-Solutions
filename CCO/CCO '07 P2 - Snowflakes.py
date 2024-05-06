"""
https://dmoj.ca/problem/cco07p2
There are 12 ways of representing each snowflake and storing all of them in a set is too memory consuming
Instead, we find a way to turn all rotations into the same form such as by creating all 12 ways and
storing the lexicographically smallest one

Example case:
2
2 2 1 2 2 2
2 1 2 2 2 2
"No two snowflakes are alike."
"""

import sys

input = sys.stdin.readline
n = int(input())
seen = set()

for _ in range(n):
    flake = list(map(int, input().split()))
    rev = list(reversed(flake))

    # take lexicographical minimum rotation/reverse
    standard = min([flake[i:] + flake[:i] for i in range(6)] + [rev[i:] + rev[:i] for i in range(6)])
    standard = tuple(standard)  # turn to tuple since lists are not hashable

    if standard in seen:
        print("Twin snowflakes found.")
        sys.exit()
    seen.add(standard)

print("No two snowflakes are alike.")
