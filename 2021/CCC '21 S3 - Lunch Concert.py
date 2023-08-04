# O(N*log(P)), using binary search
# could also get O(N*log(N)) by sorting but thats more complicated

import sys

input = sys.stdin.readline  # up to 200k lines of input, so use this

n = int(input())
pos = []
speed = []
max_range = []

for _ in range(n):
    p, s, r = map(int, input().split())
    pos.append(p)
    speed.append(s)
    max_range.append(r)


def get_time(target, pos, speed, max_range):
    diff = abs(target - pos)
    if max_range >= diff:  # can already hear it
        return 0
    else:
        return (diff - max_range) * speed


low, high = 0, 1_000_000_000
while high >= low:
    mid = low + (high - low) // 2
    middle = sum(get_time(mid, pos[i], speed[i], max_range[i]) for i in range(n))
    lower = sum(get_time(mid-1, pos[i], speed[i], max_range[i]) for i in range(n))
    upper = sum(get_time(mid+1, pos[i], speed[i], max_range[i]) for i in range(n))

    lowest = min(lower, middle, upper)
    if lowest == lower:
        high = mid - 1
    elif lowest == middle:
        # print(mid)
        print(middle)
        break
    elif lowest == upper:
        low = mid + 1

