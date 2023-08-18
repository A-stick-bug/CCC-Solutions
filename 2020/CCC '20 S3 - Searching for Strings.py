# 7/15 TLE, need rolling hash

from collections import Counter

needle = input()
permutation = Counter(needle)
haystack = input()

used = set()


def solve():
    sub = Counter(haystack[:len(needle)])

    res = 0
    if len(needle) > len(haystack):
        return 0

    for left in range(len(haystack) - len(needle) + 1):
        right = left + len(needle)-1

        if permutation == sub:
            window = tuple(haystack[left:right+1])
            if window not in used:
                res += 1
                used.add(window)

        if right != len(haystack)-1:
            sub[haystack[left]] -= 1
            sub[haystack[right+1]] += 1

    return res


print(solve())
