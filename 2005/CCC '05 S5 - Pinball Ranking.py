# 35/100 on DMOJ (with PY3), 50/100 (with PYPY3) TLE
# unsure of how this would score on CCC because it's not on CCC grader

# the proper solution probably uses a binary search tree
from bisect import bisect_right

n = int(input())
scores = []
total = 0
for i in range(1, n + 1):  # i is how many elements are in scores during this iteration
    score = int(input())
    rank = bisect_right(scores, score)  # find ranking of this score
    scores.insert(rank, score)
    total += i - rank  # reverse rank because scores is in increasing order

print(round(total / n, 2))  # get 2 decimal place average
