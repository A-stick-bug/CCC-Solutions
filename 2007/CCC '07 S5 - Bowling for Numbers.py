# DP, for each bowling pin, we can either hit it along with the next W-1 pins, or leave it
# precompute the score gained by throwing at bowling ball at each pin in O(n)

# top-down approach, too slow/memory consuming for last test case
# check c++ code for working solution
import sys

sys.setrecursionlimit(30001)
input = sys.stdin.readline


def solve(i, ball):
    if cache[i][ball] != -1:
        return cache[i][ball]
    if ball == 0 or i >= len(scores):  # out of bowling balls or out of bounds
        return 0

    cache[i][ball] = max(scores[i] + solve(i + W, ball - 1), solve(i + 1, ball))
    return cache[i][ball]


for _ in range(int(input())):  # for each test case
    N, K, W = map(int, input().split())
    arr = [int(input()) for _ in range(N)] + [0] * W  # pad arrays with 0s
    N += W

    # precompute score gained for hitting the pins from score[i] to score[i+W-1]
    scores = [0] * (N - W + 1)
    scores[0] = sum(arr[:W])
    for i in range(1, len(scores)):
        scores[i] = scores[i - 1] + arr[i + W - 1] - arr[i - 1]

    cache = [[-1] * (K + 1) for _ in range(N + 1)]
    print(solve(0, K))
