# https://dmoj.ca/problem/ccc22s2
# approach 1: give each group a number and use a dict to check who is in what group efficiently
# this is basically a disjoint set with only the find function

x = int(input())
same = [input().split() for _ in range(x)]
y = int(input())
different = [input().split() for _ in range(y)]

n = int(input())
group = {}  # person A is in group[A], basically give each group a number, so we can tell who is in which group
for i in range(n):
    a,b,c = input().split()
    group[a] = group[b] = group[c] = i  # these 3 people are in the same group

total = 0  # total violated constraints
for p1, p2 in same:
    if group[p1] != group[p2]:  # these 2 should be in the same group, constraint violated
        total += 1

for p1, p2 in different:
    if group[p1] == group[p2]:  # these 2 should be in different groups, constraint violated
        total += 1

print(total)

# # alternate solution, this one uses sets and is more confusing
# from collections import defaultdict
#
# same = defaultdict(set)
# for _ in range(int(input())):
#     a,b = input().split()
#     same[a].add(b)
#
# different = defaultdict(set)
# for _ in range(int(input())):
#     a,b = input().split()
#     different[a].add(b)
#
# res = 0
#
# # note: constraint can't be violated twice, so we remove it after being violated
# for _ in range(int(input())):
#     abc = input().split()
#     for x in abc:
#         to_remove = set()
#         for s in same[x]:
#             if s not in abc:
#                 to_remove.add(s)
#                 res += 1
#         same[x] -= to_remove  # remove after iterating because you can't remove while iterating over a set
#
#         to_remove = set()
#         for p in abc:
#             if p != x and p in different[x]:
#                 to_remove.add(p)
#                 res += 1
#         same[x] -= to_remove
#
# print(res)
