# simply game theory DP

from math import gcd


def solve(i, pile1, pile2):
    if i == n + 1:
        return (gcd(pile1, pile2) != 1) ^ (i & 1)
    if cache[pile1][pile2] != -1:
        return cache[pile1][pile2]

    # we win if we can force a losing state onto our opponent
    return not solve(i + 1, pile1 + i, pile2) or not solve(i + 1, pile1, pile2 + i)


MN = 466  # max possible number in a pile
cache = [[-1] * MN for _ in range(MN)]

while True:
    n = int(input())
    if n == 0:
        break

    ans = solve(1, 0, 0)
    if ans:
        print(f"When n={n}, A will win.")
    else:
        print(f"When n={n}, B will win.")
