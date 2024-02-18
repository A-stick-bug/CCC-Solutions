# https://dmoj.ca/problem/ccc23s2
# alternate solution using interval DP
# check other S2 code for simpler solution using expanding 2-pointers

n = int(input())
arr = list(map(int, input().split()))

inf = 1 << 30
dp = [[0] * n for _ in range(n)]  # dp[i][j]: asymmetric value of arr[i:j+1]
res = [inf] * n  # stores the best answer so far
res[0] = 0

for length in range(1, n + 1):  # length is 0-indexed, when length=0, our interval actually has length 1
    for i in range(n - length):
        j = i + length
        dp[i][j] = dp[i + 1][j - 1] + abs(arr[i] - arr[j])  # expand view, add asymmetric value
        res[length] = min(res[length], dp[i][j])

print(*res)
