# 15/15, know when to use >= or <=

first = int(input())
second = int(input())

temp = 0
count = 0

while first >= second:
    temp = first - second
    first = second
    second = temp

    count += 1

print(count+2)