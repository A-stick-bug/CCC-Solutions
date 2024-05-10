n = int(input())
freq = [0] * 5
for _ in range(n):
    s = input()
    for i in range(5):
        if s[i] == "Y":
            freq[i] += 1

res = []
best = max(freq)
for i in range(5):
    if freq[i] == best:
        res.append(i + 1)
print(*res, sep=",")
