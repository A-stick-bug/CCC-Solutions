# optimized recursion, 10/15

n = int(input())
people = int(input())


def solve(state: list, total: int):
    if len(state) == people:  # last person gets remaining pies
        return 1

    state = list(state)
    min_pie = state[-1]

    res = 0
    if min_pie == 0:
        min_pie = 1
        max_possible = n // people
    else:
        max_possible = (n - total) // (people - len(state) + 1)

    for i in range(min_pie, max_possible + 1):
        new_state = state.copy()
        new_state.append(i)
        res += solve(new_state, total + i)

    return res


print(solve([0], 0))
