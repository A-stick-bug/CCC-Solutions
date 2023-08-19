# iterative version using while loop
# start at magnification m and start zooming out
# based on the cell we reach after zooming out, we either found a crystal, must keep zooming out, or there is no crystal

crystal = [(1, 0), (2, 0), (3, 0), (2, 1)]  # (x, y) locations for where  the crystals are
possible = [(1, 1), (3, 1), (2, 2)]  # locations where there might be a crystal if you zoom in more


def is_crystal(x, y, m):
    while m > 0:
        dimensions = 5 ** (m - 1)  # length of current magnification divided by 5, use this to get new x and y
        base_x = x // dimensions  # the x, y position if you zoom OUT by 1 magnification (x5)
        base_y = y // dimensions

        # current cell is a crystal
        if (base_x, base_y) in crystal:
            return True

        # might be a crystal, zoom in more
        elif (base_x, base_y) in possible:
            x %= dimensions  # get the new x and y positions
            y %= dimensions
            m -= 1

        else:  # no crystal area
            break

    return False  # can't zoom in further, so no crystal


for _ in range(int(input())):
    m, x, y = map(int, input().split())
    if is_crystal(x, y, m):
        print("crystal")
    else:
        print("empty")


# # recursive approach, not recommended as it is completely unnecessary
# # a while loop works just as well
#
# crystal = [(1, 0), (2, 0), (3, 0), (2, 1)]  # (x, y) locations for where  the crystals are
# possible = [(1, 1), (3, 1), (2, 2)]  # locations where there might be a crystal if you zoom in more
#
#
# def is_crystal(x, y, m):
#     if m == 0:  # can't get any smaller, if we reached here, it means we reached no crystals along the way
#         return False
#
#     dimensions = 5 ** (m - 1)
#     base_x = x // dimensions
#     base_y = y // dimensions
#
#     # current cell is a crystal
#     if (base_x, base_y) in crystal:
#         return True
#
#     if (base_x, base_y) in possible:
#         return is_crystal(x % dimensions, y % dimensions, m - 1)
#
#     return False
#
#
# for _ in range(int(input())):
#     start_m, x, y = map(int, input().split())
#     if is_crystal(x, y, start_m):
#         print("crystal")
#     else:
#         print("empty")
