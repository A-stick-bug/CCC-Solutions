# https://dmoj.ca/problem/hkccc15s2
# observe the cycles

from math import lcm, gcd


def get_key(c):
    return ord(c) - ord("a")


MOD = 10 ** 9 + 7
N, M = map(int, input().split())
s = input()
t = input()

total_le = len(s) * N
g = gcd(len(s), len(t))
dup = total_le // lcm(len(s), len(t))

t_freq = [[] for _ in range(26)]
for i, v in enumerate(t):
    t_freq[get_key(v)].append(i)

s_freq = [[] for _ in range(26)]
for i, v in enumerate(s):
    s_freq[get_key(v)].append(i)

ans = 0
for c in range(26):
    s_pos = s_freq[c]
    t_pos = t_freq[c]

    t_mod_g = [0] * g
    for idx in t_pos:
        t_mod_g[idx % g] += 1

    for idx in s_pos:
        ans += t_mod_g[idx % g]

print(ans * dup)

"""
A B C A B C A B C A B C
A B C D A B C D A B C D
1, 4, 3, 2

abcdefabcdef
abcdabcdabcd
"""
