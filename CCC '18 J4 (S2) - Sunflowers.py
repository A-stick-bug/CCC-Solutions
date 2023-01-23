# 15/15

def print_flowers(flowers):
    for i in flowers:
        out = ""
        for j in i:
            out += j + " "
        print(out[:-1])


# test for increasing sequence
def check(flowers):
    if int(flowers[0][0]) > int(flowers[0][1]):
        if int(flowers[0][0]) > int(flowers[1][0]):
            return 2
        else:
            return 3
    else:
        if int(flowers[0][0]) < int(flowers[1][0]):
            return 0
        else:
            return 1


length = int(input())
flowers = []

# putting numbers in a 2D list
for i in range(length):
    flower = input().split()
    flowers.append(flower)

for i in range(check(flowers)):
    flowers = list(zip(*flowers[::-1]))

print_flowers(flowers)
