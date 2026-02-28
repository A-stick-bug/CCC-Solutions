# https://dmoj.ca/problem/ccc26s5
# 1/15 partial solution
# No idea how to solve the full problem

for _ in range(int(input())):
    N, M, K, R, C = map(int, input().split())
    if N <= 2 or M <= 2:
        print(0)
        continue

    total = (M - 2) * (N - 2)
    if R == 1 or C == 1 or R == N or C == M:
        print(total)
        continue

    sub = min(R - 1, C - 1, N - R, M - C)
    print(total - sub)
