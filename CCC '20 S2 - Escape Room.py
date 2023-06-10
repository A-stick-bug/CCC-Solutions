import sys
from collections import deque

ROWS = int(input())
COLS = int(input())
end = ROWS * COLS
graph = [[] for _ in range(end + 1)]

# constructing the graph (as a 1D array instead of 2D because it's easier to show products)
for r in range(1, ROWS + 1):
    row = map(int, input().split())
    c = 1
    for num in row:
        if num <= end:
            graph[r * c].append(num)
        c += 1

# BFS
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



# 13/15 TLE
# from collections import deque
#
#
# factors = {}
# def find_pairs(num):
#     if num in factors:
#         return factors[num]
#
#     pairs = []
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             pairs.append((i, num // i))
#             if i != num // i:
#                 pairs.append((num // i, i))
#     factors[num] = pairs
#     return pairs
#
#
# ROWS = int(input())
# COLS = int(input())
# grid = []
# for i in range(ROWS):
#     grid.append(list(map(int, input().split())))
#
# queue = deque()
# queue.append((1,1))
# visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
# no = True
#
# while queue:
#     cell = queue.popleft()
#     row = cell[0]
#     col = cell[1]
#     visited[row-1][col-1] = True
#     if row == ROWS and col == COLS:
#         print("yes")
#         no = False
#         break
#
#     pairs = find_pairs(grid[row-1][col-1])
#     for i, j in pairs:
#         if 0 <= i-1 < ROWS and 0 <= j-1 < COLS and not visited[i-1][j-1]:
#             queue.append((i,j))
#
# if no: print("no")
