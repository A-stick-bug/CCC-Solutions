# 15/15, tricky BFS
#
# approach:
# an extra copy of the map is made for cameras (more convenient than just turning them into walls)
# for all conveyors, their cell will be turned into a (row, col) tuple of the cell that it eventually leads to
# note that it is essentially a teleport because you are not taking steps on a conveyor

from collections import deque

ROWS, COLS = map(int, input().split())
graph = [list(input()) for _ in range(ROWS)]
distances = [[10000 for _ in range(COLS)] for _ in range(ROWS)]  # distances to each cell
cameras = [[False for _ in range(COLS)] for _ in range(ROWS)]  # cells that cameras can see
flag = False  # if the starting cell is covered by camera, you cannot go anywhere

# W: wall, S: start, dot: destinations+empty, C: cameras (4 directional)
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()

# handle cameras and get start
for r in range(ROWS):
    for c in range(COLS):
        cell = graph[r][c]

        if cell == "C":
            # track cells visible to camera
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                while graph[new_r][new_c] != "W":
                    if graph[new_r][new_c] == ".":
                        cameras[new_r][new_c] = True
                    if graph[new_r][new_c] == "S":
                        flag = True
                    new_r += dr
                    new_c += dc

        if cell == "S":
            q.append((r, c))
            distances[r][c] = 0


def conveyor_to_wall(array):
    rows = len(array)
    cols = len(array[0])
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    def dfs(r, c):
        if type(array[r][c]) == tuple:  # already calculated this, just use its value
            return array[r][c]
        elif array[r][c] not in directions:  # end of conveyor
            return r, c

        direction = array[r][c]
        dr, dc = directions[direction]

        array[r][c] = '#'  # mark as visited
        res = dfs(r + dr, c + dc)  # (row, col)

        if res == (r, c):  # came back to start: cycle detected, turn into wall
            array[r][c] = 'W'
        else:
            array[r][c] = res  # set to the location it leads to as a (row, col) tuple
        return res

    for r in range(rows):
        for c in range(cols):
            if array[r][c] in directions:
                r1, r2 = dfs(r, c)
                if array[r1][r2] == 'W':  # dead end or cycle
                    array[r][c] = 'W'

    return array


# do the BFS search
graph = conveyor_to_wall(graph)  # add in the precomputed values
if not flag:
    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc

            # special case where there is a conveyor: go to wherever it leads to
            if type(graph[new_r][new_c]) == tuple:
                tp_r, tp_c = graph[new_r][new_c]

                # check that conveyor actually leads to a valid location
                if graph[tp_r][tp_c] == "." and not cameras[tp_r][tp_c] and distances[tp_r][tp_c] == 10000:
                    q.append((tp_r, tp_c))
                    distances[tp_r][tp_c] = min(distances[tp_r][tp_c], distances[row][col] + 1)
                    continue

            # regular path no conveyor and not caught by camera
            if graph[new_r][new_c] == "." and not cameras[new_r][new_c] and distances[new_r][new_c] == 10000:
                q.append((new_r, new_c))
                distances[new_r][new_c] = min(distances[new_r][new_c], distances[row][col] + 1)

for r in range(ROWS):
    for c in range(COLS):
        if graph[r][c] == ".":
            print(distances[r][c] if distances[r][c] != 10000 and not flag else -1)
