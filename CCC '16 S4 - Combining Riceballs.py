# nerd DP solution (submit with pypy3 on dmoj) 15/15

N = int(input())
dp = [[0 for _ in range(402)] for _ in range(402)]
total = [0 for _ in range(402)]

res = 0
balls = list(map(int, input().split()))
for i in range(N):
    dp[i][i] = balls[i]
    res = max(res, dp[i][i])
    if i == 0:
        total[0] = dp[i][i]
    else:
        total[i] = total[i - 1] + dp[i][i]

for length in range(1, N):
    for l in range(N - length):
        r = l + length
        j = l + 1
        k = r
        while j <= k:
            if dp[l][j - 1] and dp[l][j - 1] == dp[k][r] and (j == k or dp[j][k - 1]):
                dp[l][r] = max(dp[l][r], dp[l][j - 1] + dp[j][k - 1] + dp[k][r])
                res = max(res, dp[l][r])
                break
            if total[j - 1] - total[l - 1] < total[r] - total[k - 1]:
                j += 1
            else:
                k -= 1

print(res)

# brute force 3/15 TLE (very easy to understand)

# N = int(input())
# balls = tuple(map(int, input().split()))
#
# sizes = {}
# stack = [balls]
# while stack:
#     current = stack.pop()
#     sizes[current] = max(current)  # remembers max size
#     for i in range(len(current) - 1):
#         if current[i] == current[i + 1]:
#             next = current[:i] + (current[i] + current[i + 1],) + current[i + 2:]
#             if next not in sizes:  # if not already visited
#                 stack.append(next)
#
#     for i in range(len(current) - 2):  # x, x + 2 combining
#         if current[i] == current[i + 2]:
#             next = current[:i] + (current[i] + current[i + 1] + current[i + 2],) + current[i + 3:]
#             if next not in sizes:  # if not already visited
#                 stack.append(next)
#
# max_size = max(sizes.values())
# print(max_size)
