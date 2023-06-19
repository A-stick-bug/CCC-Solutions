n = int(input())
ans = [input() for _ in range(n)]
correct = 0
for i in range(n):
    if ans[i] == input():
        correct += 1
print(correct)