limit, n = int(input()), int(input())  # max people per group, number of people
people, time = [], [0]
for _ in range(n):
    people.append(input())
    time.append(int(input()))

dp = [float('inf')] * (n + 1)
dp[0] = 0
group_size = [0] * (n + 1)

for i in range(1, n + 1):
    _max = time[i]
    for j in range(1, min(i, limit) + 1):
        if dp[i] > dp[i - j] + _max:
            dp[i] = dp[i - j] + _max
            group_size[i] = i - j
        _max = max(_max, time[i - j])

i = n
groups = []
while i > 0:
    groups.append([people[x] for x in range(group_size[i], i)])  # get the people in each group
    i = group_size[i]

print(f'Total Time: {dp[n]}')
for group in reversed(groups):
    print(' '.join(group))

# example test case
# 3
# 5
# a
# 1
# b
# 2
# c
# 5
# d
# 3
# e
# 3
