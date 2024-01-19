# https://dmoj.ca/problem/ccc20s4

s = input() * 2  # double the array as usual in a circular question
n = len(s)
hn = n // 2  # length of 1 cycle

arr = [None] * n  # turn letters into character to build PSAs
for i, v in enumerate(s):
    arr[i] = ord(v) - 65

psa = [[0] * (n + 1) for _ in range(3)]
for i in range(3):
    for c in range(1, n + 1):
        psa[i][c] = psa[i][c - 1] + (arr[c - 1] == i)
query = lambda c, l, r: psa[c][r + 1] - psa[c][l]  # get count of c in [l, r]

cnt = [arr.count(i) // 2 for i in range(3)]  # cnt[i]: occurrences of i


def solve(a, b):
    """puts a and b next to each other so c will be in a group on the other side"""
    res = 1 << 30
    for i in range(hn):  # try all split points for a and b
        # left = arr[i - cnt[a] + 1 + hn: i+1 + hn]  # SLOW: FOR DEBUGGING ONLY
        # right = arr[i+1: i + cnt[b] + 1]
        # print(left, right)

        left = [query(c, i - cnt[a] + 1 + hn, i + hn) for c in range(3)]  # all a goes here
        right = [query(c, i + 1, i + cnt[b]) for c in range(3)]  # all b goes here
        # print(left, right)

        swaps = 0
        double = min(left[b], right[a])  # double efficiency swaps: a <-> b
        left[b] -= double
        left[a] += double
        right[a] -= double
        right[b] += double
        swaps += double

        swaps += cnt[a] - left[a]  # single efficiency swaps: a <-> c, b <-> c
        swaps += cnt[b] - right[b]
        res = min(res, swaps)

    return res


# you only have to try combinations of A and B
# since C will always end up on the opposite side of the split point after swapping A and B
print(min(solve(0,1), solve(1, 0)))
