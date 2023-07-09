# 35/100 on DMOJ (with PY3), 50/100 (with PYPY3) TLE
# unsure of how this would score on CCC because it's not on CCC grader

# the proper solution probably uses a binary search tree
from bisect import bisect_right

n = int(input())
scores = []
total = 0
for i in range(1, n + 1):
    score = int(input())
    rank = bisect_right(scores, score)
    scores.insert(rank, score)
    total += i - rank

print(round(total / n, 2))
