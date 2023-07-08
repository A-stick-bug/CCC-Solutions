# dynamic programming, too hard

while True:
    ROWS, COLS = map(int,input().split())
    if ROWS == 0 and COLS == 0:
        break

    grid = [list(input()) for _ in range(ROWS)]

