# this question involves a lot of pattern finding to optimize code
# start with a simple recursion + memoization that gets 9/15
# then check if we can remove any unnecessary recursive calls to get sublinear time complexity

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
