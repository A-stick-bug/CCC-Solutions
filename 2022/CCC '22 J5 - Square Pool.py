# 15/15, O(t^3)

n = int(input())
trees = []
for _ in range(int(input())):
    r, c = map(int, input().split())
    trees.append((r, c))

trees.append((0, 0))
trees.append((n + 1, n + 1))
trees.sort()  # top to bottom

biggestSquare = 0
for i in range(len(trees)):
    horizontal = [0, n + 1]

    for j in range(i + 1, len(trees)):
        width = 0
        height = trees[j][0] - trees[i][0] - 1
        horizontal.sort() # left to right
        for k in range(1, len(horizontal)):
            width = max(width, horizontal[k] - horizontal[k - 1] - 1)
        biggestSquare = max(biggestSquare, min(height, width))
        horizontal.append(trees[j][1])

print(biggestSquare)


# 8/15 dp approach O(mn)
# n = int(input())
# grid = [[False]*n for _ in range(n)]
#
# n_trees = int(input())
# for _ in range(n_trees):
#     r,c = map(int, input().split())
#     grid[r-1][c-1] = True
#
# res = 0
# dp = [[0] * (n + 1) for _ in range(n + 1)]
#
# for r in range(1, n + 1):
#     for c in range(1, n + 1):
#         if not grid[r-1][c-1]:  # grid and dp have 0 and 1 indexing respectively
#             dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
#             res = max(res, dp[r][c])
#
# print(res)
