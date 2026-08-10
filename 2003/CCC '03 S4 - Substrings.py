# https://dmoj.ca/problem/ccc03s4
# Suffix array solution + LCP, O(n * log^2(n)), can be optimized to O(nlogn) by switching the template

def suffix_array(s):  # O(n * log^2(n))
    n = len(s)
    perm = list(range(n))

    perm.sort(key=lambda x: s[x])  # sort first character
    rank = [0] * n  # order rank by first character, equality -> tied
    for i in range(1, n):
        rank[perm[i]] = rank[perm[i - 1]] + (1 if s[perm[i]] != s[perm[i - 1]] else 0)

    p2 = 1
    while p2 < n:
        perm.sort(key=lambda x: (rank[x], rank[x + p2] if x + p2 < n else -1))  # double sorted prefix

        new_rank = [0] * n
        for i in range(1, n):  # rerank
            prev = perm[i - 1]
            cur = perm[i]
            prev_pair = (rank[prev], rank[prev + p2] if prev + p2 < n else -1)
            curr_pair = (rank[cur], rank[cur + p2] if cur + p2 < n else -1)
            new_rank[cur] = new_rank[prev] + (1 if curr_pair != prev_pair else 0)

        rank = new_rank
        if rank[perm[-1]] == n - 1:
            break
        p2 *= 2

    return perm


def kasai_lcp(s, sa=None):  # O(n)
    if sa is None:
        sa = suffix_array(s)
    n = len(s)
    rank = [0] * n  # position of s[i:] in SA, i.e. lex order
    for i, v in enumerate(sa):
        rank[v] = i

    lcp = [0] * n  # lcp is between suffixes i and i+1 in SA
    common = 0
    for i in range(n):  # loop by starting index of suffix
        if rank[i] == n - 1:
            continue
        j = sa[rank[i] + 1]  # match with next element in SA
        while i + common < n and j + common < n and s[i + common] == s[j + common]:
            common += 1
        lcp[rank[i]] = common
        if common != 0:
            common -= 1

    return lcp


def solve():
    s = input()  # padding
    n = len(s)

    sa = suffix_array(s)
    lcp = kasai_lcp(s, sa)
    total = n - sa[0]
    for i in range(1, n):
        total += (n - sa[i]) - lcp[i - 1]  # length of substring starting here minus overlap
    print(total + 1)  # +empty


t = int(input())
for _ in range(t):
    solve()

# # 15/15 Z-algorithm solution, O(n^2)
# # For each index, check for overlaps with later indices
#
# def z_algorithm(s):
#     n = len(s)
#     z = [0] * n
#     l = r = 0
#     for i in range(1, n):
#         if l <= i <= r:
#             if i + z[i - l] - 1 < r:
#                 z[i] = z[i - l]
#             else:
#                 z[i] = r - i + 1
#                 l = i
#                 for j in range(r + 1, n):
#                     if s[j - i] == s[j]:
#                         z[i] += 1
#                         r = j
#                     else:
#                         break
#         else:
#             l = i
#             for j in range(i, n):
#                 if s[j - i] == s[j]:
#                     z[i] += 1
#                     r = j
#                 else:
#                     break
#     return z
#
#
# def solve():
#     s = input()
#     n = len(s)
#     total = n * (n + 1) // 2
#     overlaps = [0] * n
#
#     for i in range(n):  # consider `i` as starting point
#         z = z_algorithm(s[i:])
#         for j in range(len(z)):
#             overlaps[i + j] = max(overlaps[i + j], z[j])
#     print(total + 1 - sum(overlaps))
#
#
# t = int(input())
# for _ in range(t):
#     solve()

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
