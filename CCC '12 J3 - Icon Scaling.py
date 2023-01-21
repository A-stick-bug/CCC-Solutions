repeats = int(input())

x = list("*x*")
y = list(" xx")
z = list("* *")

count = 0


for _ in range(repeats):
    for i in x:
        print(repeats*i,end="")
    print()

for _ in range(repeats):
    for i in y:
        print(repeats*i,end="")
    print()

for _ in range(repeats):
    for i in z:
        print(repeats*i,end="")

    print()

