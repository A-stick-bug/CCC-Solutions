# brute force go brrr

fav = int(input())
played = int(input())

# could use itertools.combinations (and set instead of list)
games = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
scores = [-1, 0, 0, 0, 0]  # -1 is placeholder, the teams are indices 1-4

for i in range(played):  # process input
    a, b, score_a, score_b = map(int, input().split())
    games.remove((a, b))  # a < b so no need to try (b, a)
    if score_a > score_b:
        scores[a] += 3
    elif score_a == score_b:
        scores[a] += 1
        scores[b] += 1
    else:
        scores[b] += 3

# do a DFS on the remaining possibilities
stack = [(scores, games)]
win_possibilities = [(0, 3), (3, 0), (1, 1)]  # possible points gained for a game
res = 0

while stack:
    state, games = stack.pop()
    # if all games have been played, check if team "fav" is winning
    if not games:
        win = True
        for i in range(len(state)):
            if state[i] >= state[fav] and i != fav:
                win = False
                break
        if win:
            res += 1
        continue

    a, b = games.pop()
    for a_points, b_points in win_possibilities:
        new_state = state.copy()
        new_state[a] += a_points
        new_state[b] += b_points
        # copy is needed otherwise modifying one array will change all others including the ones in the queue
        stack.append((new_state.copy(), games.copy()))

print(res)
