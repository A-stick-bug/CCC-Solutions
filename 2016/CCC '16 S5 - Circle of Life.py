# cellular automata rule 18, funny triangle thing (Sierpiński triangle)
# basically there is a pattern when you jump by 2^x states
# we can take advantage of this and compute 2^x steps at once in O(n)
# TC: O(N*log(T))

n, times = map(int, input().split())
state = list(map(int, list(input())))

log2 = lambda x: x.bit_length() - 1  # log2 for integers

while times > 0:
    p2 = 2 ** log2(times)
    state = [state[(i - p2) % n] ^ state[(i + p2) % n] for i in range(n)]  # jump by p2 states
    times -= p2

print("".join(map(str, state)))
