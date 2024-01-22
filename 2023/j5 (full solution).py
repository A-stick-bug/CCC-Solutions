# tricky dfs

word = input()
R = int(input())
C = int(input())
grid = [input().split() for _ in range(R)]


def search(r, c, turned, i, dr, dc):
    if not (0 <= r < R and 0 <= c < C):  # out of bounds
        return 0
    if grid[r][c] != word[i]:  # didn't match word
        return 0
    if i == len(word) - 1:  # found word
        return 1

    res = search(r + dr, c + dc, turned, i + 1, dr, dc)
    if not turned:
        res += search(r + dc, c - dr, True, i + 1, dc, -dr)  # change directions
        res += search(r - dc, c + dr, True, i + 1, -dc, dr)  # perpendicular lines have negative reciprocal slope
    return res


dir_8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
total = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == word[0]:  # matched start of word
            for dr, dc in dir_8:
                # note: we start on the second letter to prevent turning at the start
                total += search(i + dr, j + dc, False, 1, dr, dc)

print(total)
