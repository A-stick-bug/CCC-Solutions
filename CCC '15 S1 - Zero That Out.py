repeats = int(input())
stack = []

for i in range(repeats):
    value = int(input())
    if value == 0:
        stack.pop()
    else:
        stack.append(value)

total = 0
for j in stack:
    total += j

print(total)