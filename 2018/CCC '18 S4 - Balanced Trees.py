"""
this question involves a lot of pattern finding to optimize code
start with a simple recursion + memoization that gets 9/15
then check if we can remove any unnecessary recursive calls to get sublinear time complexity

Example:
n = 10

compute all these at once
|--------------|
10, 9, ..., or 6 subtrees, each with weight 1   (5*1) = 5
5 or 4 subtrees, each with weight 2             (2*1) = 2                Cache these values:
3 subtrees with weight 3                        (1*2) = 2  <-- weight of 3 has 2 possible ways to arrange subtrees
2 subtrees with weight 5                        (1*4) = 4  <-- weight of 5 has 4 possible ways to arrange subtrees
                                                total = 13
"""

from functools import cache


@cache
def solve(w):
    if w <= 2:  # base case
        return 1

    total = 0
    prev_subtree = 1
    child_weight = w // 2  # there are at least 2 subtrees, so the weight as at most w//2

    while child_weight > 0:  # child has at least weight of 1
        subtrees = w // child_weight

        # for (subtrees - prev_subtree) number of subtrees, the weight of each subtree will be the same
        total += solve(child_weight) * (subtrees - prev_subtree)

        prev_subtree = subtrees
        child_weight = w // (subtrees + 1)

    return total


n = int(input())
print(solve(n))
