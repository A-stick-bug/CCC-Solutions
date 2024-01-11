# Fibonacci style sequence DP
# for each person, we can make a group of size [1, M], use the one that takes the least time
# dp[i] is the minimum time to let the first i people through
#
# note: we don't bother with data structures/optimization since the constraints are low
# also, everything is 1-indexed for convenience
# TC: O(M^2*Q)

M = int(input())
Q = int(input())
people = [(-1, -1)] + [(input(), int(input())) for _ in range(Q)]  # (name, time), 1-indexed

prev = [0] * (Q + 1)  # keep track of previous choice to build sequence
dp = [0] * (Q + 1)

for i in range(1, Q + 1):
    best = float('inf')
    for j in range(max(1, i - M + 1), i + 1):  # try all group sizes using previously computed values
        time = max(people[j:i + 1], key=lambda x: x[1])[1] + dp[j - 1]  # (max in current group) + (previous groups)
        if time < best:
            best = time  # found better answer
            prev[i] = j - 1

    dp[i] = best

# print(prev)
# print(dp)

cur = Q
res = []
while cur != 0:
    group = []  # recreate each group
    for i in range(prev[cur] + 1, cur + 1):
        group.append(people[i][0])

    res.append(group.copy())
    cur = prev[cur]

print(f"Total Time: {dp[-1]}")
for i in reversed(res):
    print(" ".join(i))

"""
2
3
a
3
b
2
c
1

output: 5

3
5
a
1
b
2
c
5
d
3
e
3

Output: 7
"""
