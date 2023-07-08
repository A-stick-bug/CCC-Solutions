import math

tx, ty, tz = map(int, input().split())
sx, sy, sz = map(int, input().split())

x = sx - tx
y = sy - ty
z = sz - tz

closest = x ** 2 + y ** 2 + z ** 2
while True:
    distance, turn = input().split()
    distance = int(distance)

    newX = x - distance

    if newX * x < 0:
        closest = min(closest, y ** 2 + z ** 2)
    else:
        closest = min(closest, newX**2 + y ** 2 + z ** 2)
    x = newX
    if turn == 'L':
        x, y, z = y, -x, z
    elif turn == 'R':
        x, y, z = -y, x, z
    elif turn == 'U':
        x, y, z = z, y, -x
    elif turn == 'D':
        x, y, z = -z, y, x
    if turn == 'E':
        break

print(round(math.sqrt(closest), 2))
