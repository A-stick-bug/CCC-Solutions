# interesting intervals question
# knowing what to sort by is important, also keep track of latest previous ending interval

import sys

input = sys.stdin.readline
L = int(input())
n = int(input())

intervals = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(L, L)]
intervals.sort(key=lambda x: (x[0], x[1]))

prev = 0
best = 0
for i in range(1, len(intervals)):
    prev = max(prev, intervals[i - 1][1])
    best = max(best, intervals[i][0] - prev)

print(best)
