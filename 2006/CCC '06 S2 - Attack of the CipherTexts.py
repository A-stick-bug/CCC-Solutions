# using dict + handling corner case

plain = input()
cipher = input()
s = input()

letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
table = {}
p = set(plain)
c = set(cipher)
for a, b in zip(plain, cipher):
    table[b] = a

if len(table) == 26:  # if all letters but 1 are given, we know what the last letter maps to
    mp = list(letters - p)[0]
    mc = list(letters - c)[0]
    table[mc] = mp

res = []
for char in s:
    if char in table:
        res.append(table[char])
    else:
        res.append(".")

print(*res, sep="")
