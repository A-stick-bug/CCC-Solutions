# DFS solution, technically using dynamic programming

rows = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
rows1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: "J"}

sheets = [[]]  # extra row and column because of 1-indexing
for i in range(10):
    sheets.append([0] + input().split())

# format in a way that is easier to do a DFS on
for i in range(1, 11):
    for j in range(1, 10):
        if sheets[i][j].isnumeric():  # just a number
            sheets[i][j] = int(sheets[i][j])
        else:
            temp = sheets[i][j].split("+")
            # turn into a (row, col) tuple of the sum of other cells
            sheets[i][j] = list(map(lambda exp: (rows[exp[0]], int(exp[1])), temp))


# cells are invalid if it forms a cycle (with itself or other cells)
def dfs(row, col, dependencies):
    cell = sheets[row][col]
    if (row, col) in dependencies or cell == "*":  # cycle detected or undefined cell
        return '*'

    if type(cell) == int:
        return cell
    else:
        total = 0
        dependencies.add((row, col))
        for r, c in cell:
            value = dfs(r, c, dependencies)
            if value == '*':
                return '*'
            total += value
        dependencies.remove((row, col))
        sheets[row][col] = total  # update value to prevent wasting time recalculating
        return total


for i in range(1, 11):
    for j in range(1, 10):
        sheets[i][j] = dfs(i, j, set())

for i in range(1, 11):
    print(*sheets[i][1:], sep=" ")  # don't include the extra column
