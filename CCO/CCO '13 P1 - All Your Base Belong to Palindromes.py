def convert(n, base):
    res = []
    while n > 0:
        d, rem = divmod(n, base)
        res.append(rem)
        n = d
    return res


n = int(input())

r = []
for k in range(1, int(n**0.5)+1):
    b = (n-1)//k
    if b == 0 or b==1:
        continue

    a = convert(n, b)
    if a == a[::-1]:
        r.append(b)
    if b <= 2:
        break

for b in range(2, int(n**0.5)+1):
    a = convert(n, b)
    if a == a[::-1]:
        r.append(b)

print(*sorted(set(r)), sep="\n")
