# 15/15, don't forget to 'break'

total = int(input())
repeats = int(input())

times = []
count = 0

for _ in range(repeats):
    x = int(input())
    times.append(x)

times.sort()

for i in times:
    total -= i
    if total < 0:
        print(count)
        break

    count += 1