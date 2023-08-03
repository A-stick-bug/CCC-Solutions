# optimized recursion + memoization, 15/15

n = int(input())
people = int(input())

# notice how solve([1,2,4,4]) and solve([1,3,3,4]) will return the same thing because they have the same:
# (length, last value, total), so that's what we need to memoize
memo = {}


def solve(state: list, total: int):
    check = (len(state), state[-1], total)  # check if we can reuse our previous calculations
    if check in memo:
        return memo[check]

    if len(state) == people:  # last person gets remaining pies, only 1 possibility
        return 1

    min_possible = state[-1]  # the minimum number of pies that the next person can receive
    res = 0

    if min_possible == 0:  # 0 means this is the first person getting pie
        min_possible = 1
        max_possible = n // people
    else:
        max_possible = (n - total) // (people - len(state) + 1)

    # starting at min_possible makes sure that we only go through valid states (pruning invalid branches)
    for i in range(min_possible, max_possible + 1):
        new_state = state.copy()
        new_state.append(i)
        res += solve(new_state, total + i)

    # memoize states as a tuple
    store_state = (len(state), state[-1], total)
    memo[store_state] = res

    return res


print(solve([0], 0))


# # more efficient, but less intuitive, tabulation (bottom-up) approach, 15/15
# n = int(input())
# people = int(input())
# dp = [[0 for _ in range(people + 1)] for _ in range(n + 1)]
#
# for i in range(1, people + 1):
#     dp[i][i] = 1
#
# for i in range(1, n + 1):
#     for j in range(1, min(i, people + 1)):
#         dp[i][j] += dp[i - 1][j - 1] + dp[i - j][j]
#
# print(dp[n][people])
