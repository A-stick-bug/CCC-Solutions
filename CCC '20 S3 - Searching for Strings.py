# 7/15 TLE, need rolling hash

from collections import Counter

needle = input()
needle_count = Counter(needle)
haystack = input()

used = set()


def solve():
    res = 0
    if len(needle) > len(haystack):
        return 0
    for i in range(0, len(haystack)-len(needle)+1):
        window = tuple(haystack[i:i+len(needle)])
        sub = Counter(window)
        if needle_count == sub and window not in used:
            res += 1
            used.add(window)

    return res


print(solve())
