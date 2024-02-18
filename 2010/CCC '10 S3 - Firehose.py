"""
https://dmoj.ca/problem/ccc10s3
Similar logic to https://leetcode.com/problems/maximize-the-minimum-powered-city
Probably the hardest S3

Binary search the answer: check if it is possible for the max to be less than X
- Each hydrant covers X on both sides, so 2X total, use greedy to decide where to place it
- Note that since the locations are circular, we don't know where to start, so we start at all locations: O(N^2)

TC: O(N^2*log(MN))
"""

MN = 10 ** 6  # circumference
N = int(input())
locs = sorted([int(input()) for _ in range(N)])
H = int(input())


def works(x, start):
    """check if the max distance can be less than X, given the index of the starting house to cover"""
    houses = locs[start:] + list(map(lambda x: x + MN, locs[:start]))  # wrap the houses around
    covers = -1
    used = 0
    for house in houses:
        if house > covers:  # house is too far from previous hydrant, need to place a new one
            used += 1
            covers = house + 2 * x  # greedy idea: place it as far as possible for max covering
        if used > H:
            return False
    return True


def check_all(x):  # for every house, try to start by covering it with a hydrant
    return any(works(x, i) for i in range(N))


low = 0  # template binary search on shortest hydrant length possible
high = MN // 2
while low <= high:
    mid = (low + high) // 2
    if check_all(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)
