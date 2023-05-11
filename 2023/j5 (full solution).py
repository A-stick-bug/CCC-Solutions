# no palindromes so no need to track the words that are already found

word = input()
ROWS = int(input())
COLS = int(input())

grid = []
for i in range(ROWS):
    grid.append(input().split())

count = 0
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def check(row, col, dr, dc, index, turned):
    global count
    if ROWS > row >= 0 and COLS > col >= 0 and grid[row][col] == word[index]:
        # found the word
        if index == len(word) - 1:
            count += 1
            return

        # continue checking in direction
        check(row + dr, col + dc, dr, dc, index + 1, turned)

        # check perpendiculars
        if not turned:
            check(row - dc, col + dr, -dc, dr, index + 1, True)
            check(row + dc, col - dr, dc, -dr, index + 1, True)


for i in range(ROWS):
    for j in range(COLS):
        # if current tile matches first letter of word, search in all 8 directions
        if grid[i][j] == word[0]:
            for r, c in directions:
                check(i + r, j + c, r, c, 1, False)

print(count)
