# order statistics tree (implemented with fenwick tree)
# TLE on DMOJ because python is too slow, but the code is correct (checked with code below)

import sys
from math import log2


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def select(self, k):  # "traversal" in log(n)
        i = 0
        l2 = int(log2(self.size)) + 1
        for power in reversed(range(l2)):
            # 1<<x = 2 to the power of x
            if i + (1 << power) <= self.size and self.tree[i + (1 << power)] < k:
                i += 1 << power
                k -= self.tree[i]
        return i + 1


input = sys.stdin.readline
n = int(input())

queries = []
scores = set()
for _ in range(n):
    q = input().split()
    if q[0] != "Q":
        scores.add(int(q[2]))  # get unique scores
    queries.append(q)

scores = sorted(scores, reverse=True)  # sort in reverse because rank 1 has HIGHEST score
compress = {val: i + 1 for i, val in enumerate(scores)}  # 1-indexed ranks

rtp = {}  # maps a ranking to a person
ptr = {}  # map a person to their ranking

bit = FenwickTree(len(scores) + 1)
for q in queries:
    if q[0] == "Q":
        k_th_rank = bit.select(int(q[1]))
        person = rtp[k_th_rank]
        print(person)

    elif q[0] == "N":
        person, score = map(int, q[1:])
        rank = compress[score]
        rtp[rank] = person
        ptr[person] = rank
        bit.update(rank, 1)

    elif q[0] == "M":
        person, score = map(int, q[1:])
        new_rank = compress[score]
        bit.update(ptr[person], -1)  # remove current rank
        bit.update(new_rank, 1)
        ptr[person] = new_rank
        rtp[new_rank] = person


# # order statistics tree (implemented with fenwick tree)
# # TLE on DMOJ, so I compare the output to the actual test data myself
#
# import sys
# from math import log2
#
# for case in range(1, 7):
#     sys.stdin = open(f'Wowow/wowow{case}.in', 'r')
#
#
#     class FenwickTree:
#         def __init__(self, size):
#             self.size = size
#             self.tree = [0] * (size + 1)
#
#         def update(self, i, diff):
#             while i <= self.size:
#                 self.tree[i] += diff
#                 i += i & -i
#
#         def select(self, k):  # "traversal" in log(n)
#             i = 0
#             l2 = int(log2(self.size)) + 1
#             for power in reversed(range(l2)):
#                 # 1<<x = 2 to the power of x
#                 if i + (1 << power) <= self.size and self.tree[i + (1 << power)] < k:
#                     i += 1 << power
#                     k -= self.tree[i]
#             return i + 1
#
#
#     n = int(input())
#     queries = []
#     scores = set()
#     for _ in range(n):
#         q = input().split()
#         if q[0] != "Q":
#             scores.add(int(q[2]))  # get unique scores
#         queries.append(q)
#
#     scores = sorted(scores, reverse=True)  # sort in reverse because rank 1 has HIGHEST score
#     compress = {val: i + 1 for i, val in enumerate(scores)}  # 1-indexed ranks
#
#     rtp = {}  # maps a ranking to a person
#     ptr = {}  # map a person to their ranking
#
#     ANSWER = []
#
#     bit = FenwickTree(len(scores) + 1)
#     for q in queries:
#         if q[0] == "Q":
#             k_th_rank = bit.select(int(q[1]))
#             person = rtp[k_th_rank]
#             # print(person)
#             ANSWER.append(person)
#
#         elif q[0] == "N":
#             person, score = map(int, q[1:])
#             rank = compress[score]
#             rtp[rank] = person
#             ptr[person] = rank
#             bit.update(rank, 1)
#
#         elif q[0] == "M":
#             person, score = map(int, q[1:])
#             new_rank = compress[score]
#             bit.update(ptr[person], -1)  # remove current rank
#             bit.update(new_rank, 1)
#             ptr[person] = new_rank
#             rtp[new_rank] = person
#
#     sys.stdin = open(f'Wowow/wowow{case}.out', 'r')
#     CORRECT = [int(input()) for _ in range(len(ANSWER))]
#
#     print(ANSWER == CORRECT)
