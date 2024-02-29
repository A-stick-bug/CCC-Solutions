import sys
from collections import Counter


def solve():
    s = input().strip()
    freq = Counter(s)
    for i in range(1, N):
        if freq[s[i]] == 1 and freq[s[i - 1]] == 1:
            print("F")
            return
        if freq[s[i]] != 1 and freq[s[i - 1]] != 1:
            print("F")
            return
    print("T")


input = sys.stdin.readline
T, N = map(int, input().split())
for _ in range(T):
    solve()
