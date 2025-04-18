# https://dmoj.ca/problem/cco08p3
# Encode rooted tree recursively in a 'standardized' way and check equality

import sys

MOD = 1_000_000_007
base = 10_007
encode = lambda num: num + base - 1

input = sys.stdin.readline

# construct the 2 trees
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    l, r = map(int, input().split())
    graph[i] = [l, r]

m = int(input())
graph2 = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    l, r = map(int, input().split())
    graph2[i] = [l, r]


def normalize(graph):
    def solve(cur):
        if cur < 0:  # leaf
            return encode(cur)
        l = solve(graph[cur][0])
        r = solve(graph[cur][1])

        # hopefully l != r when the subtrees are not equal
        if l > r:
            l, r = r, l  # generalize: smaller one first
        return (l * base + r) % MOD

    return solve(1)


a = normalize(graph)
b = normalize(graph2)
if a == b:
    print("Fred and Mary might have the same mobile.")
else:
    print("Fred and Mary have different mobiles.")

"""
3
2 3
-1 -2
-3 -4
3
2 3
-1 -3
-2 -4
different
"""
