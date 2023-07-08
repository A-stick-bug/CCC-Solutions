from math import ceil, floor

amount = int(input())

i = 1
spaces = (amount - 1) * 2

# first half + middle
while i <= ceil(amount / 2):

    for a in range(0, i + (i - 1)):
        print("*", end="")

    for j in range(0, spaces):
        print(" ", end="")

    for a in range(0,i+(i-1)):
        print("*", end="")

    print()

    spaces -= 4
    i += 1

# second half excluding middle
i = 1
asterisk = amount - 2
spaces = 4
while i <= floor(amount/2):
    for a in range(0, asterisk):
        print("*", end="")
    for j in range(0, spaces):
        print(" ", end="")
    for a in range(0, asterisk):
        print("*", end="")

    print()

    i += 1
    spaces += 4
    asterisk -= 2

