# binary search solution, a binary search tree would be better but this works
from bisect import bisect_right

gates = [i for i in range(1, int(input()) + 1)]  # list of all available gates
n = int(input())

res = 0
for _ in range(n):
    plane = int(input())
    curr = bisect_right(gates, plane)  # find the maximum possible gate this plane can occupy
    if curr == 0:  # smaller than all available, therefore, it cannot land
        break
    else:
        res += 1
        gates.pop(curr - 1)  # remove that gate because the current planes occupies it (doesn't TLE!!!)

print(res)


# weird sorting method (not my idea)
# gates = int(input())
# n = int(input())
# planes = [(int(input()) - 1, i) for i in range(n)]
# planes.sort()
#
# res, time = 0, float('inf')
# for plane, order in planes:
#     if order < time and res < plane:
#         res += 1
#     else:
#         time = min(time, order)
# print(res)


# brute force, 7/15, TLE
# def find_gate(right):
#     for i in reversed(range(right+1)):
#         if not gates[i]:
#             gates[i] = True
#             return True
#     return False
#
#
# gates = [False for _ in range(int(input()))]  # False = no plane, True = occupied
# n = int(input())
# res = 0
#
# for i in range(n):
#     plane = int(input()) - 1
#     if not find_gate(plane):  # couldn't find a gate to put plane
#         break
#     else:
#         res += 1
#
# print(res)
