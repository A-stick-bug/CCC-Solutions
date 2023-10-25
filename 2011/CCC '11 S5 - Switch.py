# Brute force BFS, save memory by converting state to base 10 number
# Optimization: remove leading and trailing zeros (they don't affect anything)
# Time complexity: O(n * 2^n)
# O(2^n) possible states, O(n) to copy state

from collections import deque
import sys

pow2 = [2 ** i for i in range(25)]  # precompute powers of 2 for speed


def compress(state):
    """compress state into a base 10 integer to save memory"""
    res = 0
    for i in reversed(range(len(state))):
        if state[i]:
            res += pow2[i]
    return res


def off(arr):
    """turn off 4+ in a row lights"""
    arr.append(0)  # extra zero to ensure trailing ones are handled
    ones = 0
    for i, val in enumerate(arr):
        if val:
            ones += 1
        else:
            if ones >= 4:  # more than 4 in a row, turn them off
                for j in range(i - ones, i):
                    arr[j] = 0
            ones = 0

    # optimization: remove leading and trailing zeros
    while len(arr) > 4 and not arr[-1]:
        arr.pop()
    arr = arr[::-1]
    while len(arr) > 4 and not arr[-1]:
        arr.pop()
    return arr[::-1]


n = int(input())
arr = [int(input()) for _ in range(n)]
arr = off(arr)  # turn off 4+ in a row lights

used = set()
q = deque([(0, arr)])
while q:
    flips, state = q.popleft()
    if not sum(state):
        print(flips)
        sys.exit()

    # turn on any light for the next state
    for i in range(len(state)):
        if state[i]:  # light is already on
            continue

        # create new state and turn off more than 4 in a row lights
        new_state = state.copy()
        new_state[i] = 1
        new_state = off(new_state)

        cs = compress(new_state)  # convert from binary to int to save memory
        if cs not in used:
            used.add(cs)
            q.append((flips + 1, new_state))
