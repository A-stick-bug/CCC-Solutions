"""
15/15 solution, using Fenwick Tree (BIT) and coordinate compression
Submit with PYPY on DMOJ or else TLE

- first, we must compress the coordinates to its relative size, eg. [1, 1, 100, 10000] --> [0, 0, 1, 2]
- now that all elements are small, we can create an empty BIT with just enough spots for every unique element
  (frequency array)
- then, we can find the rank of each element in log(n) and insert it in log(n)

"""

from sys import stdin

input = stdin.readline


class FenwickTree:
    def __init__(self, size):  # create empty BIT
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res


n = int(input())

# precompute the ranks (basically coordinate compression)
scores = [int(input()) for _ in range(n)]
ordered = sorted(list(set(scores)))
rank = {ordered[i]: i for i in range(len(ordered))}

total = 0
bit = FenwickTree(n)

for i in range(1, n + 1):  # i is how many elements are in scores during this iteration
    # use the rank, not the actual value
    score = rank[scores[i - 1]]
    place = bit.query(score + 1)  # 1-indexed queries so +1
    total += i - place  # reverse rank because scores are in increasing order

    bit.update(score + 1, 1)  # add the new score by increasing its count by 1

print(round(total / n, 2))  # get 2 decimal place average

"""
# Old brute force code (50/100 on DMOJ)
from bisect import bisect_right

n = int(input())
scores = []
total = 0
for i in range(1, n + 1):  # i is how many elements are in scores during this iteration
    score = int(input())
    rank = bisect_right(scores, score)  # find ranking of this score
    scores.insert(rank, score)
    total += i - rank  # reverse rank because scores are in increasing order

print(round(total / n, 2))  # get 2 decimal place average
"""
