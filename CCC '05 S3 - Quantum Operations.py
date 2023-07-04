# 15/15, tricky 2D array manipulation

n = int(input())
matrices = []

for _ in range(n):  # taking in input
    rows, cols = map(int, input().split())
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    matrices.append(matrix)


def multiply(mat2, mat1):
    r1, c1 = len(mat1), len(mat1[0])
    r2, c2 = len(mat2), len(mat2[0])
    tr, tc = r1 * r2, c1 * c2
    res = [[0] * tc for _ in range(tr)]

    for r in range(r1):
        for c in range(c1):
            cell = mat1[r][c]
            for rr in range(r2):
                for cc in range(c2):
                    res[rr + (r2 * r)][cc + (c2 * c)] = cell * mat2[rr][cc]
    return res


for i in range(1, n):
    matrices[i] = multiply(matrices[i], matrices[i - 1])

# getting the 6 values
ans = matrices[-1]
r, c = len(ans), len(ans[0])
rows = [0 for _ in range(r)]
cols = [0 for _ in range(c)]
_min = float('inf')
_max = -float('inf')

for i in range(r):
    for j in range(c):
        cell = ans[i][j]
        _min = min(_min, cell)
        _max = max(_max, cell)
        rows[i] += cell
        cols[j] += cell

print(_max, _min, max(rows), min(rows), max(cols), min(cols), sep="\n")
