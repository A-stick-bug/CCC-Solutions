number = int(input())
zero = int(input())

total = number

for _ in range(zero):
    total += number*10
    number *= 10

print(total)