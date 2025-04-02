# https://dmoj.ca/problem/cco08p5
# Binary packaging + bitmask 1/32 optimization
# DP to compute the amount of candy we can be taking
# Since we must use all candies, we can take X and the rest goes to the other person
# Note that this also creates a symmetry, so we only check half the states
#
# TC: O(n * logC * T/32), T = sum of all weights ~ 10^7

LG = 9  # 2^9 = 512

n = int(input())
dp = 1
total = 0

for _ in range(n):
    cnt, val = map(int, input().split())
    total += cnt * val

    # binary packaging
    for pow2 in range(LG + 1):
        w = 1 << pow2
        if cnt > w:
            cnt -= w
            dp |= dp << (w * val)
        else:
            dp |= dp << (cnt * val)
            break

best = 1 << 30
dp = bin(dp)[2:]  # string for O(1) index checking
for i in range(total // 2 + 1):
    if dp[i] == "1":
        best = min(best, abs(total - i - i))  # we take `i`, other takes `total - i`
print(best)
