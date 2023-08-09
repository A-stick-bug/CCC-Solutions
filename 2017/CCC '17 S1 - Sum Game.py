from itertools import accumulate

n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

team1 = list(accumulate(team1))
team2 = list(accumulate(team2))

res = 0
for i in reversed(range(n)):
    if team1[i] == team2[i]:
        res = i+1
        break

print(res)
