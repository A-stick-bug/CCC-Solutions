# could've used a dict for coordinate change for each direction
# for example {"l": [-1, 0], "r": [1, 0], "d": [0, -1], "u": [0, 1]}

point = [-1, -5]
used = {(3, -5), (5, -5), (0, -7), (2, -7), (1, -3), (7, -5), (6, -7), (-1, -5), (4, -7), (3, -3), (5, -3), (0, -2),
        (0, -1), (1, -7), (7, -3), (7, -6), (-1, -6), (4, -5), (3, -7), (3, -4), (5, -7), (5, -4), (0, -3), (2, -3),
        (7, -7), (6, -3), (7, -4), (-1, -7)}

move = input().split()
danger = False

while True:
    move[1] = int(move[1])
    x = point[0]
    y = point[1]

    if move[0] == "l":
        for i in range(1, move[1] + 1):
            if (x - i, y) not in used:
                used.add((x - i, y))
            else:
                danger = True
        x -= move[1]

    elif move[0] == "r":
        for i in range(1, move[1] + 1):
            if (x + i, y) not in used:
                used.add((x + i, y))
            else:
                danger = True
        x += move[1]

    elif move[0] == "u":
        for i in range(1, move[1] + 1):
            if (x, y + i) not in used:
                used.add((x, y + i))
            else:
                danger = True
        y += move[1]

    elif move[0] == "d":
        for i in range(1, move[1] + 1):
            if (x, y - i) not in used:
                used.add((x, y - i))
            else:
                danger = True
        y -= move[1]

    elif move[0] == "q":
        break

    if danger:
        print(f"{x} {y} DANGER")
        break
    else:
        print(f"{x} {y} safe")

    point = [x, y]
    move = input().split()

