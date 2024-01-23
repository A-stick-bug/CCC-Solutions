# https://dmoj.ca/problem/cco10p4
# extension of the knapsack problem
# instead of just taking or not taking, we must transition from the previous type

def solve():
    components = int(input())
    n = int(input())
    types = [list(map(int, input().split())) for _ in range(n)]
    types.sort(key=lambda x: x[2])  # sort by type so we can get items in order

    budget = int(input())
    dp = [[0] * (budget + 1) for _ in range(components)]  # dp[type][cost] contains the best value so far
    for cost, value, t in types:
        t -= 1  # 0-indexing
        for c in reversed(range(budget + 1)):
            if c - cost < 0:
                break
            dp[t][c] = max(dp[t][c], dp[t - 1][c - cost] + value)  # typical knapsack transition

    print(dp[-1][budget])


solve()
