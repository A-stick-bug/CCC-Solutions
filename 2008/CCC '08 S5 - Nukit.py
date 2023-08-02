# recursion + memoization
# inspired by MMHS solution: http://mmhs.ca/ccc/2008/CCC2008J5NukitRecursion.txt
# Patrick goes first, the first person to be unable to do a reaction loses

from functools import cache

# each element is how much of a, b, c, and d are removed from the reaction
reactions = [[2, 1, 0, 2], [1, 1, 1, 1], [0, 0, 2, 1], [0, 3, 0, 0], [1, 0, 0, 1]]


# memoize to avoid recalculating and save time, also avoids making a 31^4 dp array
@cache
def can_win(a, b, c, d):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return False

    win = True
    for aa, bb, cc, dd in reactions:
        if can_win(a - aa, b - bb, c - cc, d - dd):
            win = False

    return win


for _ in range(int(input())):
    vals = list(map(int, input().split()))
    w = can_win(*vals)
    print("Roland" if w else "Patrick")
