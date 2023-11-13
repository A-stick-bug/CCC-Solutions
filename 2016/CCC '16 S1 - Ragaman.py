# finding the difference between 2 strings

from collections import Counter

s1 = Counter(input())
s2 = Counter(input())

diff = 0
res = 0
for char, count in s1.items():
    diff = count - s2[char]
    if diff < 0:
        res = float('inf')
    else:
        res += diff

print("A" if res <= s2["*"] else "N")
