# https://dmoj.ca/problem/ccc26s4
# Lesson learned from this question: spend more time making observations before throwing data structures
# Basically all ideas in this problem work because of some monotonic invariant
#
# Problem reduces to: minimize mx = max(number of smaller numbers to the right, over all indices)
# We define a record as an index where the prefix max increases
#
# Observations:
# - mx must occur at a record, due to monotonicity
# - this allows us to effectively ignore non-records in our calculations (keeping zeros),
#   leaving us with an increasing sequence with zeros in between (hint: monotonic property is useful again here)
#
# Binary search on mx:
# - We greedily assign spare gems from the left, using a monotonic queue to track how many
#   gems we need to assign
# - the offset variable allows us to increase/decrease all numbers currently in the queue by an offset
#
# TC: O(n*log(n))


from itertools import accumulate
from collections import deque


class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, diff):
        idx += 3  # simple offset
        while idx < len(self.bit):
            self.bit[idx] += diff
            idx += idx & (-idx)

    def query(self, idx):
        total = 0
        idx += 3
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total


def works(mx):  # check if having a max of mx is possible
    if mx < max(nxt):
        return False
    spare = K
    cur = 0  # current record
    q = deque()
    offset = 0

    for i in range(len(filtered)):
        if filtered[i] != 0:
            while q and mx - filtered_nxt[i] <= q[-1][1] + offset:
                q.pop()
            q.append([filtered[i], mx - filtered_nxt[i] - offset])
            while q and q[0][1] + offset == 0:
                old, _ = q.popleft()
                cur = old
        else:
            if spare - cur < 0:
                return False
            spare -= cur

            offset -= 1
            while q and q[0][1] + offset == 0:
                old, _ = q.popleft()
                cur = old
    return True


N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # padding
MN = 10 ** 6 + 10

# compute number of elements to the right that are smaller
nxt = [0] * (N + 1)
bit = Fenwick(MN)
for i in reversed(range(N + 1)):
    if arr[i] == 0:
        continue
    move = bit.query(arr[i] - 1)
    nxt[i] = move
    bit.update(arr[i], 1)

# get records
pref = list(accumulate(arr, func=max))
filtered = []  # this represents all elements that are actually important
filtered_nxt = []
for i in range(1, N + 1):
    if pref[i] != pref[i - 1]:
        filtered.append(pref[i])
        filtered_nxt.append(nxt[i])
    elif arr[i] == 0:
        filtered.append(0)
        filtered_nxt.append(0)

# print(filtered_nxt)
# print(filtered)

low = 0
high = N
ans = high
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)

"""
Example cases:
records are the numbers [5 6 8]

8 10
5 4 6 3 2 8 7 7
Output: 3

7 10
5 0 6 0 0 8 7
Output: 2

7 11
5 0 6 0 0 8 7
Output: 1
"""
