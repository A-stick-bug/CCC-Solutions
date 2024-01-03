# just casework with while loop

n = int(input())
turn = 0

first = int(input())
second = int(input())
third = int(input())

while n > 0:
    if turn % 3 == 0:
        first += 1
        if first == 35:
            n += 30
            first = 0

    elif turn % 3 == 1:
        second += 1
        if second == 100:
            n += 60
            second = 0

    else:
        third += 1
        if third == 10:
            n += 9
            third = 0

    turn += 1
    n -= 1

print(f"Martha plays {turn} times before going broke.")
