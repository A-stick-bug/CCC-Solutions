# both mobiles can be thought of as a tree
# it can be proven that if every layer of the 2 mobiles have the same amount of each ornament (order doesn't matter),
# then there exists a way to rearrange them to match the other mobile (maybe?)

# based on the fact that the test cases pass, this SHOULD be true, unsure about cases like this one though
# 3
# 2 3
# -1 -2
# -3 -4
# 3
# 2 3
# -1 -3
# -2 -4

from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# construct the 2 trees
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    l, r = map(int, input().split())
    graph[i].extend([l, r])

m = int(input())
graph2 = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    l, r = map(int, input().split())
    graph2[i].extend([l, r])

# do a breadth first search of each layer on both trees and check if they match
q = deque([1])
q2 = deque([1])

for layer in range(200_000):  # process each layer seperately
    cur_layer = defaultdict(int)  # ornaments in the current layer (unordered)
    cur_layer2 = defaultdict(int)

    if not q:  # already processed the entire thing and all layers matched
        print("Fred and Mary might have the same mobile.")
        break

    for i in range(len(q)):  # go through all elements in the current layer
        node = q.popleft()
        for adj in graph[node]:
            if adj < 0:  # if the value is negative, it is an ornament which we need to match with the other tree
                cur_layer[adj] += 1
            else:
                q.append(adj)

    for i in range(len(q2)):  # do the same thing for the other tree
        node = q2.popleft()
        for adj in graph2[node]:
            if adj < 0:
                cur_layer2[adj] += 1
            else:
                q2.append(adj)

    if cur_layer != cur_layer2:  # if any layer doesn't match, we know that the 2 trees are different
        print("Fred and Mary have different mobiles.")
        break
