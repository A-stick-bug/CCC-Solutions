# greedy approach, passes original CCC cases but fails new DMOJ cases
# [O negative, O positive, A negative, A positive, B negative, B positive, AB negative, AB positive]

available = list(map(int, input().split()))
req = list(map(int, input().split()))
res = 0

for i in range(len(req)):
    for j in range(i,-1,-1):
        # B cannot get A
        if (i == 4 or i == 5) and (j == 2 or j == 3):
            continue

        # negative cannot get positive
        elif i % 2 == 0 and j % 2 == 1:
            continue

        if available[j] > req[i]:
            res += req[i]
            available[j] -= req[i]
            break
        else:
            res += available[j]
            req[i] -= available[j]
            available[j] = 0

print(res)
