# 3/15, simple recursion

from math import log, ceil

n = int(input())
layers = ceil(log(n, 3)) - 1


def filter(low, high, layer):
    if layer == layers:
        for i in range(low, high + 1):
            print(i)
        return

    section = (high - low) // 3
    filter(low, low + section, layer + 1)
    filter(high - section, high, layer + 1)


filter(0, n, 0)
