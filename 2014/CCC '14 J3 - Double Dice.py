times = int(input())

p1 = 100
p2 = 100

i = 0
while i < times:
    x = input()
    x = x.split(None, 1)

    if int(x[0]) > int(x[1]):
        p2 -= int(x[0])
    elif int(x[1]) > int(x[0]):
        p1 -= int(x[1])

    i += 1

print(p1)
print(p2)