# https://dmoj.ca/problem/cco00p3
# Standard game theory DP
# Note:
# - the time complexity isn't that bad
# - a lot of states are actually invalid since the max sum is 31

from functools import cache

n = 6


def solve():
    s = list(map(int, input()))

    freq = [4] * n
    for val in s:  # moves that already happened
        freq[val - 1] -= 1

    @cache
    def can_win(state, total):
        for i in range(n):  # check if we can force opponent to lose
            if state[i] > 0 and total + (i + 1) <= 31:
                new_state = list(state)
                new_state[i] -= 1
                if not can_win(tuple(new_state), total + (i + 1)):
                    return True
        return False

    if can_win(tuple(freq), sum(s)) ^ (len(s) % 2):  # |s| % 2 to check whose turn it is
        print("A")
    else:
        print("B")


for _ in range(int(input())):
    solve()
