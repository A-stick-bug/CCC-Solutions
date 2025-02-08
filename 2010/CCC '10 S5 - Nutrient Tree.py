# TLE, CHECK C++ CODE FOR EXPLANATIONS
# https://dmoj.ca/problem/ccc10s5

from collections import Counter

MN = 102  # max number of nodes
MS = 520000  # max sum of values
ME = 725  # max enhancements to ever put on and edge


def find_next_end(start):
    for i in range(start, len(s)):
        if s[i] in ") ":
            return i
    return len(s)


s = input()
X = int(input())
idx = 0
graph = [[] for _ in range(MN)]
node_idx = 0
amt = Counter()

# turn into tree
stack = []
while idx < len(s):
    # print(idx, stack)
    if s[idx] == "(":  # start of group
        idx += 1
    elif s[idx] == " ":  # empty space?
        idx += 1
    elif s[idx] == ")":  # end group
        a = stack.pop()
        b = stack.pop()
        graph[node_idx].append(a)
        graph[node_idx].append(b)
        stack.append(node_idx)
        node_idx += 1
        idx += 1
    else:  # number
        nxt_idx = find_next_end(idx)
        num = int(s[idx:nxt_idx])
        stack.append(node_idx)
        amt[node_idx] = num
        node_idx += 1
        idx = nxt_idx

root = node_idx - 1
n = node_idx

# print(graph)
# print(amt)
# print(f"{root=}")
# for i in range(len(graph)):
#     for j in graph[i]:
#         print(i, j)

dp = [[-1] * (X + 1) for _ in range(n)]

for cur in range(n):
    if not graph[cur] and cur not in amt:  # empty node
        continue

    for rem in range(X + 1):
        if cur in amt:  # base case: leaf
            best = 0
            low = 0
            high = min(rem, ME) if cur != root else 0

            while low <= high:
                mid = (low + high) // 2
                to_top = mid
                to_cur = rem - to_top
                best_v = amt[cur] + to_cur

                if cur == root:
                    best = max(best, best_v)  # no need to send to top
                best = max(best, min((1 + to_top) ** 2, best_v))

                if (1 + to_top) ** 2 >= best_v:  # sending too much to the top
                    high = mid - 1
                else:  # sending too little to the top
                    low = mid + 1

            dp[cur][rem] = best
            continue

        best = 0
        low = 0
        high = min(rem, ME) if cur != root else 0
        while low <= high:
            mid = (low + high) // 2
            to_top = mid

            to_child = rem - to_top
            c1, c2 = graph[cur]
            best_v = 0
            for to_c1 in range(to_child + 1):
                to_c2 = to_child - to_c1
                v1 = dp[c1][to_c1]
                v2 = dp[c2][to_c2]
                best_v = max(best_v, v1 + v2)

            if cur == root:
                best = max(best, best_v)  # no need to send to top
            best = max(best, min((1 + to_top) ** 2, best_v))

            if (1 + to_top) ** 2 >= best_v:  # sending too much to the top
                high = mid - 1
            else:  # sending too little to the top
                low = mid + 1

        dp[cur][rem] = best

print(dp[root][X])

# # recursive code for reference (this is missing the binary search in base case)
# # https://dmoj.ca/problem/ccc10s5
#
# import sys
# from collections import Counter
#
# sys.setrecursionlimit(100000)
# MN = 102
# inf = 1 << 30
#
# MS = 520000  # max sum of values
# ME = 725  # max enhancements to ever put on and edge
#
#
# def find_next_end(start):
#     for i in range(start, len(s)):
#         if s[i] in ") ":
#             return i
#     return len(s)
#
#
# s = input()
# X = int(input())
# idx = 0
# graph = [[] for _ in range(MN)]
# node_idx = 0
# amt = Counter()
#
# # turn into tree
# stack = []
# while idx < len(s):
#     # print(idx, stack)
#     if s[idx] == "(":  # start of group
#         idx += 1
#     elif s[idx] == " ":  # empty space?
#         idx += 1
#     elif s[idx] == ")":  # end group
#         a = stack.pop()
#         b = stack.pop()
#         graph[node_idx].append(a)
#         graph[node_idx].append(b)
#         stack.append(node_idx)
#         node_idx += 1
#         idx += 1
#     else:  # number
#         nxt_idx = find_next_end(idx)
#         num = int(s[idx:nxt_idx])
#         stack.append(node_idx)
#         amt[node_idx] = num
#         node_idx += 1
#         idx = nxt_idx
#
# root = node_idx - 1
# n = node_idx
#
# # print(graph)
# # print(amt)
# # print(f"{root=}")
# # for i in range(len(graph)):
# #     for j in graph[i]:
# #         print(i, j)
#
# dp = [[-1] * (X + 1) for _ in range(n)]
#
#
# def solve(cur, rem):
#     if dp[cur][rem] != -1:  # cache
#         return dp[cur][rem]
#
#     if cur in amt:  # base case: leaf
#         best = 0
#         for to_top in range(min(rem, ME) + 1):  # binary searchable
#             to_cur = rem - to_top
#             if cur == root:
#                 best = max(best, amt[cur] + to_cur)  # no need to send to top
#             best = max(best, min((1 + to_top) ** 2, amt[cur] + to_cur))
#         dp[cur][rem] = best
#         return best
#
#     best = 0
#
#     low = 0
#     high = min(rem, ME) if cur != root else 0
#     while low <= high:
#         mid = (low + high) // 2
#         to_top = mid
#
#         to_child = rem - to_top
#         c1, c2 = graph[cur]
#         best_v = 0
#         for to_c1 in range(to_child + 1):
#             to_c2 = to_child - to_c1
#             v1 = solve(c1, to_c1)
#             v2 = solve(c2, to_c2)
#             best_v = max(best_v, v1 + v2)
#
#         if cur == root:
#             best = max(best, best_v)  # no need to send to top
#         best = max(best, min((1 + to_top) ** 2, best_v))
#
#         if (1 + to_top) ** 2 >= best_v:  # sending too much to the top
#             high = mid - 1
#         else:  # sending too little to the top
#             low = mid + 1
#
#     dp[cur][rem] = best
#     return best
#
#
# print(solve(root, X))
