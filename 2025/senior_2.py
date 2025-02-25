s = input()
n = int(input())  # 0-index

res = []
for c in s:
    if c.isalpha():
        res.append([c, 0])
    else:
        res[-1][1] = res[-1][1] * 10 + int(c)

total = sum(j for i,j in res)
n %= total

for c, freq in res:
    if n < freq:
        print(c)
        break
    else:
        n -= freq

"""
a4b1c2d10
100

r2d2
8
"""