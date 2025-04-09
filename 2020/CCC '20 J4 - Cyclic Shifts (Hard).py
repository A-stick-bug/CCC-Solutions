"""
https://dmoj.ca/problem/ccc20j4
https://dmoj.ca/problem/ccc20j4hard
Check if string `T` contains a cyclic shift of `S`
Length of both strings is at most N

Cheese solution: O(N^2)
- Brute force each cyclic shift of `S`
- Check if the cyclic shift is in `T` using Python's built in .find()

Set solution: O(N^2)
- Store all cyclic shifts of `S` in a set
- Try all substring of length |S| in `T` and check with the set

Set solution + hashing: O(N), high constant factor
- replace all substring extraction operations with hashing for O(1)

Z-algorithm solution: O(N), low constant factor
- the cyclic shift can be broken into 2 parts: 1 suffix and 1 prefix of `s`
- if the prefix + suffix match >= m, it is a complete cyclic shift
"""

import sys


def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if l <= i <= r:
            # fully within a larger matching segment, reuse answer
            if i + z[i - l] - 1 < r:
                z[i] = z[i - l]

            # extends to the end of a matching segment, check if we can extend farther
            else:
                z[i] = r - i + 1
                l = i
                # start from `r` since before that already matches
                for j in range(r + 1, n):
                    if s[j - i] == s[j]:
                        z[i] += 1
                        r = j
                    else:
                        break
        # manually match
        else:
            l = i
            for j in range(i, n):
                if s[j - i] == s[j]:
                    z[i] += 1
                    r = j
                else:
                    break
    return z


t = input()
s = input()
n, m = len(t), len(s)

pre_match = s + "!" + t
suf_match = s[::-1] + "!" + t[::-1]
pre_z = z_algorithm(pre_match)[m + 1:]
suf_z = z_algorithm(suf_match)[m + 1:][::-1]

# print(pre_z)
# print(suf_z)

for i in range(n - 1):
    # for example, suf=CDE pre=AB -> full cyclic shift
    if suf_z[i] + pre_z[i + 1] >= m:
        print("yes")
        sys.exit()
print("no")

# # 9/10 hashing solution
# import sys
# from itertools import accumulate
#
# # max possible length of anything string
# # all hashes are aligned with this maximum length
# MN = 400001
#
#
# class SubstringHash:
#     def __init__(self, arr, p=29, mod=10 ** 9 + 7):
#         arr = [ord(i) - ord("a") + 1 for i in arr]
#
#         # precompute powers of `p`, with MOD
#         self.mod = mod
#         self.power = [0] * MN
#         self.power[0] = 1
#         for i in range(1, MN):
#             self.power[i] = (self.power[i - 1] * p) % self.mod
#
#         # precompute hashes of each character in `str1`
#         n = len(arr)
#         self.psa = [0] * (n + 1)
#         for i in range(1, n + 1):
#             self.psa[i] = (arr[i - 1] * self.power[MN - i] + self.psa[i - 1]) % self.mod
#
#     def query(self, l, r):  # query hash of [l,r]
#         # shift up to match `mn`
#         hs = (self.psa[r + 1] - self.psa[l]) * self.power[l] % self.mod
#         return hs
#
#
# t = input()
# s = input()
# n, m = len(t), len(s)
# s *= 2
#
# hash_s = SubstringHash(s, mod=1152921504606846989)
# hash_t = SubstringHash(t, mod=1152921504606846989)
# shifts = set()
# for i in range(m):
#     shifts.add(hash_s.query(i, i + m - 1))
#
# # print(shifts)
# for i in range(n - m + 1):
#     if hash_t.query(i, i + m - 1) in shifts:
#         print("yes")
#         sys.exit()
#
# print("no")
