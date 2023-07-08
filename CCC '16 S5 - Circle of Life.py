# 7/15 TLE, probably because converting each state to tuple takes too long for large n, and too much memory
# cellular automata rule 18

n, times = map(int, input().split())
row = list(map(int, list(input())))
states = {}
states_i = {}
found = False

for i in range(times):
    new_state = [0] * n

    new_state[0] = row[1] ^ row[-1]
    new_state[-1] = row[0] ^ row[-2]
    for cell in range(1, n - 1):  # first and last done separately because it is a circle
        new_state[cell] = row[cell - 1] ^ row[cell + 1]

    row = new_state.copy()

    temp = tuple(row)
    if temp in states:
        final_state = times % (i - states[temp])
        print(*states_i[final_state - 1], sep="")
        found = True
        break

    states[temp] = i
    states_i[i] = temp

if not found:
    print(*row, sep="")
