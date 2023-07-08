# just have to make individual code for each test case, hard part if figuring out those cases
# not finished, currently 2/15


def palindrome(rows, cols, rp, cp):
    grid = [["a" for _ in range(cols)] for _ in range(rows)]
    if (rp == rows and cp < cols) or (cp == cols and rp < rows):
        return "IMPOSSIBLE"

    elif rp == rows and cp == cols:
        return grid

    elif rp == 0 and cp == 0:
        for col in range(cols):
            grid[0][col] = "b"
        for row in range(rows):
            grid[row][0] = "b"
        grid[0][0] = "z"
        return grid

    # generating palindromes
    for i in range(rp):
        for j in range(cols):
            grid[i][j] = "b"
    for j in range(cp):
        for i in range(rows):
            grid[i][j] = "b"

    if rp == 0:
        for i in range(1,cols-cp+1):
            grid[0][-i] = "z"
    elif cp == 0:
        for i in range(1,rows-rp+1):
            grid[-1][i] = "z"

    return grid


x = list(map(int, input().split()))
output = palindrome(*x)
for i in output:
    if output == "IMPOSSIBLE":
        print(output)
        break
    else:
        print("".join(i))
