# THIS IS NOT THE FULL SOLUTION
#
# https://dmoj.ca/problem/ccc19s4
# part of my pre-2024 CCC partial mark grind
# will probably add full solution later

n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_DAY = (n + k - 1) // k  # "using fewest days possible" means we must use this many days

# notice that the 2 subtasks don't overlap, this is subtask 1
if 1 and 2 * k >= n:
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
# transition: dp[i][k] -> dp[i+1][]
else:
    from functools import cache
    @cache
    def solve(i, day):
        if day > MAX_DAY:
            return -(1<<60)
        if i == n:
            if day == MAX_DAY:
                return 0
            else:
                return -(1<<60)
        cm = 0
        best = 0
        for j in range(i, min(n,i+k)):
            cm = max(cm, arr[j])
            best = max(best, cm + solve(j+1, day + 1))
        return best

    print(solve(0, 0))
