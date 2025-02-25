from collections import defaultdict
import sys
from bisect import insort, bisect_left

input = sys.stdin.readline
N, M, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]  # color, pretty

vals = defaultdict(list)  # by color
for a, b in arr:
    vals[a].append(b)

for v in vals:  # padding
    vals[v].append(-1)
    vals[v].sort()

# MAINTAIN THESE
minimum = sorted(([v[-1] for v in vals.values()]))
second = sorted(([v[-2] for v in vals.values()]))
total = sum(v[-1] for v in vals.values())

for _ in range(Q + 1):
    if _ != 0:
        t, i, x = map(int, input().split())
        i -= 1  # 0-index

        # remove old
        old_c, old_v = arr[i]
        if t == 1:  # color of i becomes x
            arr[i][0] = x
        else:  # prettiness of i becomes x
            arr[i][1] = x
        new_c, new_v = arr[i]

        minimum.pop(bisect_left(minimum, vals[old_c][-1]))
        second.pop(bisect_left(second, vals[old_c][-2]))
        total -= vals[old_c][-1]
        vals[old_c].pop(bisect_left(vals[old_c], old_v))

        if old_c != new_c:
            minimum.pop(bisect_left(minimum, vals[new_c][-1]))
            second.pop(bisect_left(second, vals[new_c][-2]))
        total -= vals[new_c][-1]

        # add new
        if old_c != new_c:
            insort(minimum, vals[old_c][-1])
            insort(second, vals[old_c][-2])
        total += vals[old_c][-1]

        insort(vals[new_c], new_v)
        insort(minimum, vals[new_c][-1])
        insort(second, vals[new_c][-2])
        total += vals[new_c][-1]

    print(total + max(0, (second[-1] - minimum[0])))

"""
6 3 0
1 6
2 9
3 4
2 7
3 9
1 3

3 2 2
1 20
2 30
1 10
1 3 2
2 3 25
"""
