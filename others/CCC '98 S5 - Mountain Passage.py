# the grid is technically weighted (weights can be 0 or 1)
# therefore, we need to use Dijkstra's algorithm

# -1 O2, if the current elevation or the next elevation > grid[1][1]
# also, we can only go to adjacent cells with an absolute difference of less than 3

import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
test_cases = int(input())

for case in range(1, test_cases + 1):
    n = int(input())
    grid = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grid[i][j] = int(input())
    lowest = grid[1][1]  # elevation at which no oxygen is needed

    found_path = False
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    visited[1][1] = True  # starting locationrg
    pq = [(0, 1, 1)]  # (cost, row, col)

    while pq:
        cost, row, col = heapq.heappop(pq)
        if row == n and col == n:  # found path to end
            found_path = True
            print(cost)

        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if 0 < new_r <= n and 0 < new_c <= n and not visited[new_r][new_c]:  # not out of bounds
                dz = abs(grid[row][col] - grid[new_r][new_c])  # difference in elevation
                if dz > 2:
                    continue

                visited[new_r][new_c] = True
                new_cost = cost + (grid[row][col] > lowest or grid[new_r][new_c] > lowest)
                heapq.heappush(pq, (new_cost, new_r, new_c))

    if not found_path:
        print("CANNOT MAKE THE TRIP")

    if case != test_cases:  # a new line is needed after each test case, except for the last test case
        print()
