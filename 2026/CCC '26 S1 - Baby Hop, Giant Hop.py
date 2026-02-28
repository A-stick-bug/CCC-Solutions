# https://dmoj.ca/problem/ccc26s1
# This question is a lot of casework, but we can just put all possible candidates into a list
# Then get the second-smallest moves

A, B, K, T = [int(input()) for _ in range(4)]
dif = abs(A - B)

big = dif // K
small = dif % K

options = [big + small,
           big + 1 + (big + 1) * K - dif,
           big + small + 2,
           big + 1 + (big + 1) * K - dif + 2,
           dif,
           ]
if big != 0:
    options.extend([big - 1 + dif - (big - 1) * K,
                    big - 1 + dif - (big - 1) * K + 2])
options = sorted(set(options))

print(options[T - 1])
