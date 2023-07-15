x_max, y_max = map(int, input().split())
x, y = 0, 0

while True:
    dx, dy = map(int, input().split())
    if dx == 0 and dy == 0:
        break

    x += dx
    y += dy

    # stay in boundaries
    x = max(x, 0)
    x = min(x, x_max)
    y = max(y, 0)
    y = min(y, y_max)
    print(x, y)
