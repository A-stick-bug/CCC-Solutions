# cellular automata rule 18, funny triangle thing (Sierpiński triangle)

n, times = map(int, input().split())
row = list(map(int, list(input())))


def log2(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result


while times > 0:
    new_state = []
    p2 = 2 ** log2(times)

    for i in range(n):
        left = (i - p2) % n  # use mod because it is circular, this will automatically 'wrap around the edges'
        right = (i + p2) % n
        cell = row[left] ^ row[right]  # each state is the XOR of its neighbours
        new_state.append(cell)

    row = new_state.copy()
    times -= p2

print(*row, sep="")
