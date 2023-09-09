# method 2, 15/15: compress matrix graph into a 1D adjacency list
import sys
from collections import deque

ROWS = int(input())
COLS = int(input())
end = ROWS * COLS
graph = [[] for _ in range(end + 1)]

# constructing the graph
for r in range(1, ROWS + 1):
    row = map(int, input().split())
    c = 1
    for num in row:
        if num <= end:
            graph[r * c].append(num)  # avoid having to factor
        c += 1

# simple BFS on adjacency list
visited = [False for _ in range(end + 1)]
visited[1] = True
q = deque([1])

while q:
    current = q.popleft()

    if current == end:
        print("yes")
        sys.exit()  # end code

    for adj in graph[current]:
        if not visited[adj]:
            visited[adj] = True
            q.append(adj)

print("no")


# # Brute force, 13/15 TLE, this would pass if it was written in c++
# # The cache part is very important
#
# from collections import deque
# import sys
# from functools import cache
#
# input = sys.stdin.readline
#
#
# @cache
# def find_pairs(num):
#     pairs = []
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             pairs.append((i, num // i))
#             if i != num // i:
#                 pairs.append((num // i, i))
#     return pairs
#
#
# ROWS = int(input())
# COLS = int(input())
# grid = []
# for i in range(ROWS):
#     grid.append(list(map(int, input().split())))
#
# q = deque()
# q.append((1, 1))
# visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
# visited[0][0] = True
# no = True
#
# while q:
#     row, col = q.popleft()
#
#     if row == ROWS and col == COLS:
#         print("yes")
#         no = False
#         break
#
#     pairs = find_pairs(grid[row - 1][col - 1])
#     for i, j in pairs:
#         if 0 <= i - 1 < ROWS and 0 <= j - 1 < COLS and not visited[i - 1][j - 1]:
#             visited[i - 1][j - 1] = True
#             q.append((i, j))
#
# if no:
#     print("no")
