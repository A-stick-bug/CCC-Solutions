# Simple BFS question but a 2D array is used instead of a graph

from collections import deque

x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())

q = deque()
q.append((x1,y1))

directions = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
distance = [[float('inf') for _ in range(9)] for _ in range(9)]
distance[x1][y1] = 0

visited = [[False for _ in range(9)] for _ in range(9)]

while q:
    x,y = q.popleft()
    if x == x2 and y == y2:
        print(distance[x][y])
        break
    visited[x][y] = True
    for dx, dy in directions:
        new_x, new_y = dx+x, dy + y
        if 1 <=new_x <= 8 and 1 <= new_y <= 8 and not visited[new_x][new_y]:
            q.append((new_x,new_y))
            distance[new_x][new_y] = min(distance[new_x][new_y], distance[x][y] + 1)
