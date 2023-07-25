# 15/15, inefficient and lazy solution
# barely passes, 0.05 seconds from time limit

from itertools import product
import sys

M = int(input())  # max number of string segments in sequence
N = int(input())
a = [input() for _ in range(N)]
b = [input() for _ in range(N)]

seq = list(range(N))
all_combinations = []  # generate every possible sequence
for i in range(1,M):
    all_combinations.extend(list(product(seq, repeat=i)))

for comb in all_combinations:  # test all of them
    s1 = [a[i] for i in comb]
    s2 = [b[i] for i in comb]
    if "".join(s1) == "".join(s2):
        print(len(comb))
        for i in comb:
            print(i+1)  # +1 because question uses 1 indexing
        sys.exit()

print("No solution.")


# # TLE on last test case, I expected this to be faster but I guess not
# # do a BFS and try combinations until one is found (does not use any nerd string algorithms)
#
# import sys
# from collections import deque
#
# M = int(input())  # max number of string segments in sequence
# N = int(input())
# a = [input() for _ in range(N)]
# b = [input() for _ in range(N)]
#
# q = deque([[]])  # start with empty string
#
# while q:
#     seq = q.popleft()
#     if len(seq) >= M:
#         break
#
#     for new in range(N):
#         new_seq = seq + [new]
#         s1 = [a[i] for i in new_seq]
#         s2 = [b[i] for i in new_seq]
#         if "".join(s1) == "".join(s2):
#             print(len(new_seq))
#             for i in new_seq:
#                 print(i + 1)  # +1 because question uses 1 indexing
#             sys.exit()
#         q.append(new_seq)
#
# print("No solution.")