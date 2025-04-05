# https://dmoj.ca/problem/ccc03s4
# Unique solution using the Z-algorithm
# For each index, check for overlaps with later indices

def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if l <= i <= r:
            if i + z[i - l] - 1 < r:
                z[i] = z[i - l]
            else:
                z[i] = r - i + 1
                l = i
                for j in range(r + 1, n):
                    if s[j - i] == s[j]:
                        z[i] += 1
                        r = j
                    else:
                        break
        else:
            l = i
            for j in range(i, n):
                if s[j - i] == s[j]:
                    z[i] += 1
                    r = j
                else:
                    break
    return z


def solve():
    s = input()
    n = len(s)
    total = n * (n + 1) // 2
    overlaps = [0] * n

    for i in range(n):  # consider `i` as starting point
        z = z_algorithm(s[i:])
        for j in range(len(z)):
            overlaps[i + j] = max(overlaps[i + j], z[j])
    print(total + 1 - sum(overlaps))


t = int(input())
for _ in range(t):
    solve()

# # 9/15 hashing solution, O(n^2)
# import string
#
# # max possible length of anything string
# # all hashes are aligned with this maximum length
# MN = 5001
# mp = {char: idx + 1 for idx, char in enumerate(string.ascii_lowercase + string.ascii_uppercase + string.digits)}
#
#
# class SubstringHash:
#     def __init__(self, arr, p=29, mod=10 ** 9 + 7):
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
# t = int(input())
# for _ in range(t):
#     sub = set()
#
#     s = [mp[i] for i in input()]
#     n = len(s)
#     s = SubstringHash(s, p=67, mod=1152921504606846989)
#     for i in range(n):
#         for j in range(i, n):
#             sub.add(s.query(i, j))
#     print(len(sub) + 1)

# # 9/15 trie solution: O(n^2)
#
# def solve():
#     s = input()
#     trie = {}
#
#     def add_word(word):
#         cur = trie
#         for char in word:
#             if char in cur:
#                 cur = cur[char]
#             else:
#                 cur[char] = {}
#                 cur = cur[char]
#
#     for i in range(len(s)):
#         add_word(s[i:])
#
#     tot = 0
#     stack = [trie]
#     while stack:
#         cur = stack.pop()
#         tot += 1
#         for adj in cur.values():
#             stack.append(adj)
#     print(tot)
#
#
# for _ in range(int(input())):
#     solve()
