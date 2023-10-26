n = int(input())
row1 = [0] + list(map(int, input().split()))
row2 = [0] + list(map(int, input().split()))

total = 0

for i in range(1, n + 1):
    if row1[i] == 1:
        if row1[i - 1] == 1:
            total += 1
        else:
            total += 3

for i in range(1, n + 1):
    if row2[i] == 1:
        total += 3
        if row2[i - 1] == 1:
            total -= 2
        if i % 2 == 1 and row1[i] == 1:
            total -= 2

print(total)
