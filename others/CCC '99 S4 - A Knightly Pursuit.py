from collections import deque

inf = 10_000_000

directions = [
    (-2, -1), (-2, 1), (2, -1), (2, 1),
    (-1, -2), (-1, 2), (1, -2), (1, 2)
]


for _ in range(int(input())):
    ROWS, COLS, pr, pc, kr, kc = [int(input()) for _ in range(6)]

    kr = ROWS - kr
    kc -= 1

    moves = [[inf] * COLS for _ in range(ROWS)]
    visited = [[False] * COLS for _ in range(ROWS)]
    visited[kr][kc] = True

    q = deque([(kr, kc)])
    moves[kr][kc] = 0

    while q:
        row, col = q.popleft()

        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc

            if 0 <= new_r < ROWS and 0 <= new_c < COLS and not visited[new_r][new_c]:
                q.append((new_r, new_c))
                visited[new_r][new_c] = True
                moves[new_r][new_c] = moves[row][col] + 1

    win = stalemate = inf
    move = 0

    for j in reversed(range(ROWS - pr + 1)):
        if moves[j][pc - 1] % 2 == move % 2 and moves[j][pc - 1] <= move and j != 0:
            win = min(win, move)
        elif moves[j][pc - 1] % 2 == (move - 1) % 2 and moves[j][pc - 1] < move:
            stalemate = min(stalemate, move - 1)
        move += 1

    if win != inf:
        print(f"Win in {win} knight move(s).")
    elif stalemate != inf:
        print(f"Stalemate in {stalemate} knight move(s).")
    else:
        print(f"Loss in {move - 2} knight move(s).")
