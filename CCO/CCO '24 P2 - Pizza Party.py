# https://dmoj.ca/problem/cco24p2
# (this question is hard to explain)
# make as few LCS as possible to fully match 2 lists (draw lines between same elements)
# note that LCS on unique elements is basically LIS on the indices

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


# solution that assumes there are only 2 types of pizza
def solve_1_2():
    if a == b[::-1]:  # stack is perfectly arranged already
        print(1)
        print(*[1] * n)
        print(*[1] * n)
    else:  # put all 1 in a stack and all 2 in a stack
        print(2)
        print(*a)
        print(*b)


# solution that assumes all a_i is unique
def solve_unique():
    loc = [-1] * (n + 1)
    for i, v in enumerate(b):
        loc[v] = i
    stacks = []
    ordered = SortedList()  # index lower bound, location in stacks

    put_on = [-1] * n  # stack to put i-th pizza
    in_stack = [-1] * (n + 1)  # stack that i is in

    for i, val in enumerate(reversed(a)):
        idx = ordered.lower_bound((loc[val], 0)) - 1
        if idx < 0:  # need to make new stack
            ordered.insert((loc[val], len(stacks)))
            stacks.append([val])
            put_on[i] = len(stacks)
            in_stack[val] = len(stacks)
        else:  # put in stack greedily, given [1,3,6], we put 4 after 3 since we wasted the least amount of space
            old = ordered[idx]
            stacks[old[1]].append(val)
            put_on[i] = old[1] + 1  # 1-indexed
            in_stack[val] = old[1] + 1
            ordered.insert((loc[val], old[1]))  # update value
            ordered.pop(ordered.lower_bound(old))

    res = [0] * n
    for i, v in enumerate(b):
        res[i] = in_stack[v]
    print(len(stacks))
    print(*put_on[::-1])  # reverse since making a stack from an array reverses the elements
    print(*res)


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sorted(a) != sorted(b):  # pizzas don't match
    print(-1)
elif len(set(a)) == n:
    solve_unique()
else:
    solve_1_2()

"""
Custom test cases:
5
1 2 4 3 5
5 1 4 2 3

3
3 2 2 1 1
1 3 2 2 1
"""
