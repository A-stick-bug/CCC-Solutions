map = {}

same = []
x = int(input())
for _ in range(x):
    same.append(input().split())

diff = []
y = int(input())
for _ in range(y):
    diff.append(input().split())

z = int(input())
for i in range(z):
    a, b, c = input().split()
    map[a] = i
    map[b] = i
    map[c] = i

broke = 0
for i in same:
    if map[i[0]] != map[i[1]]:
        broke += 1
for i in diff:
    if map[i[0]] == map[i[1]]:
        broke += 1

print(broke)
