# 5/15

import sys


class FenwickTree:  # uses 1-indexing, point update, range query
    def __init__(self, nums: list[int]):
        """Create a Fenwick tree using a Prefix Sum Array"""
        psa = [0] * (len(nums) + 1)  # first create a PSA
        for i in range(1, len(nums) + 1):
            psa[i] = psa[i - 1] + nums[i - 1]  # assuming nums is 0-indexed

        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):  # create BIT using PSA
            self.bit[i] = psa[i] - psa[i - (i & -i)]  # MUST HAVE PARENTHESIS ON (i & -i)!!!

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def query_range(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
N, M, Q = map(int, input().split())

ls = list(map(int, input().split()))
lines = [[] for _ in range(M + 1)]  # the stations in line i
for s, l in enumerate(ls, start=1):
    lines[l].append(s)

people = list(map(int, input().split()))
##### END INPUT #####

bit = FenwickTree(people)
people.insert(0, 0)  # 1-indexed

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:  # range query
        l, r = q[1:]
        print(bit.query_range(l, r))

    else:  # move everything in the line to the right
        line = lines[q[1]]  # shift everything on the line
        ln = len(line)
        old = people[line[-1]]
        for i in reversed(range(ln - 1)):
            s1, s2 = line[i], line[i + 1]
            bit.update(s2, -people[s2] + people[s1])  # move s1 to s2
            people[s2] = people[s1]
        bit.update(line[0], -people[line[0]] + old)  # wrap the start and end
        people[line[0]] = old
