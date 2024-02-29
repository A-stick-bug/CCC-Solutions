import sys

input = sys.stdin.readline

n = int(input())
hf = n // 2

arr = [int(input()) for _ in range(n)] * 2
t = 0
for i in range(n):
    if arr[i] == arr[i + hf]:
        t += 1
print(t)
