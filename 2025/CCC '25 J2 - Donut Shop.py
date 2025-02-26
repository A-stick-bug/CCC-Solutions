donuts = int(input())

n = int(input())
for _ in range(n):
    operation = input()
    change = int(input())

    if operation == "+":
        donuts += change
    else:
        donuts -= change

print(donuts)
