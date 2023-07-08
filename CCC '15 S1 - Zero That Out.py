repeats = int(input())
stack = []

for i in range(repeats):
    value = int(input())
    if value == 0:
        stack.pop()
    else:
        stack.append(value)

count = 0
for j in stack:
    count += j

print(count)