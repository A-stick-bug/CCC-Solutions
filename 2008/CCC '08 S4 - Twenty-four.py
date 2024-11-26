# https://dmoj.ca/problem/ccc08s4
# Brute force recursion
# Optimizations:
# - sort the state to represent a set of numbers (order doesn't matter)
# - cache to prevent re-computation

from functools import cache


@cache
def solve(state):
    if len(state) == 1:  # base case: 1 number left
        return 0 if state[0] > 24 else state[0]

    mx = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if i == j:
                continue
            a, b = state[i], state[j]
            for oper in ["*", "+", "-", "//"]:
                if oper == "//" and (b == 0 or a % b != 0):
                    continue
                res = eval(f"{a}{oper}{b}")
                new_state = tuple(sorted([state[k] for k in range(len(state)) if k != i and k != j] + [res]))
                mx = max(mx, solve(new_state))

    return mx


t = int(input())
for _ in range(t):
    arr = tuple(sorted(int(input()) for _ in range(4)))
    print(solve(arr))
