def crystalSquaresatX(m, x):
    if m >= 1:
        power = 5 ** (m - 1)
        location = x // power
        if location == 0 or location == 4:  # no crystal
            return 0

        elif location == 1 or location == 3:  # columns 1 and 3
            return 1 * power + crystalSquaresatX(m - 1, x % power)

        elif location == 2:  # middle column
            return 2 * power + crystalSquaresatX(m - 1, x % power)
    return 0


for t in range(int(input())):
    m, x, y = map(int, input().split())
    if y < crystalSquaresatX(m, x):
        print("crystal")
    else:
        print("empty")
