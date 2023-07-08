number = int(input())
zero = int(input())

count = number

for _ in range(zero):
    count += number * 10
    number *= 10

print(count)