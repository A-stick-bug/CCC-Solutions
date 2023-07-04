flooring = int(input())
rows = int(input())
cols = int(input())

grid = [list(input()) for _ in range(rows)]
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(r, c):
    stack = [(r,c)]
    area = 0
    while stack:
        row, col = stack.pop()
        if grid[row][col] != ".":
            continue

        grid[row][col] = "x"
        area += 1
        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                stack.append((new_r, new_c))
    return area


areas = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            areas.append(dfs(i,j))

rooms_covered = 0
areas.sort(reverse=True)
for a in areas:
    if flooring - a < 0:
        break
    flooring -= a
    rooms_covered += 1

# apparently, if theres only enough for one room, you must remove the s (test case 5)
print(f"{rooms_covered} rooms, {flooring} square metre(s) left over") if rooms_covered != 1 else print(f"1 room, {flooring} square metre(s) left over")
