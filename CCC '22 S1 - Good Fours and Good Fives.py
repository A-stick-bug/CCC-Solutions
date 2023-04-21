num = int(input())
count = 0
if num % 5 == 0:
    count += 1
while num > 0:
    if num % 4 == 0:
        count += 1
    num -= 5

print(count)
