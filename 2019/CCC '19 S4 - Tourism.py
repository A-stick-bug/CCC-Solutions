# WORK IN PROGRESS
#
# https://dmoj.ca/problem/ccc19s4
# part of my pre-2024 CCC partial mark grind
# will probably add full solution later
# at most 1.5N dp cells will be used

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
n = 1000
k = 2
arr = [1] * n

MAX_DAY = (n + k - 1) // k  # "using fewest days possible" means we must use this many days
inf = 1 << 30

# notice that the 2 subtasks don't overlap, this is subtask 1
if 2 * k >= n:
    prefix, suffix, both = [0], [0], [0]
    for i in range(n):
        if i < k and (n - i - 1) < k:
            both.append(arr[i])
        elif i < k:
            prefix.append(arr[i])
        else:
            suffix.append(arr[i])

    both.sort(reverse=True)
    bp = max(prefix)
    bb1 = both[0]
    if len(both) > 1 and k != n:
        bb2 = both[1]
    else:
        bb2 = 0
    bs = max(suffix)

    print(max(bp + bs, bp + bb1, bs + bb1, bb1 + bb2))

# brute force DP, subtask 2
else:
    dp = [[-inf] * (MAX_DAY + 1) for _ in range(n + 1)]
    dp[n][MAX_DAY] = 0  # base case

    for i in reversed(range(n)):
        for day in reversed(range(MAX_DAY)):
            # if not i*k <=
            cm = 0
            for j in range(i, min(n, i + k)):
                cm = max(cm, arr[j])
                dp[i][day] = max(dp[i][day], cm + dp[j + 1][day + 1])

    print(dp[0][0])

    t = 0
    for i in range(n + 1):
        for j in range(MAX_DAY + 1):
            t += dp[i][j] == -inf
    print(t)
