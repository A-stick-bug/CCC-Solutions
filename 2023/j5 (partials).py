# 6/15 perpendicular turns not solved
# what I came up with during the actual CCC

word = list(input())
y = int(input())
x = int(input())

puzzle = []

for i in range(y):
    to_add = input().split()
    puzzle.append(to_add)

cols = list(zip(*puzzle))
for i in range(len(cols)):
    cols[i] = list(cols[i])

count = 0
length = len(word)

for row in puzzle:
    for i in range(len(row)-length + 1):
        if word == row[i:i+length] or word[::-1] == row[i:i+length]:
            count += 1

for col in cols:
    for i in range(len(col)-length + 1):
        if word == col[i:i+length] or word[::-1] == col[i:i+length]:
            count += 1

diagonal1 = [[] for _ in range(y-1+x)]
diagonal2 = [[] for _ in range(y-1+x)]
minimum = -y + 1

for a in range(x):
    for b in range(y):
        diagonal1[a + b].append(puzzle[b][a])
        diagonal2[a - b - minimum].append(puzzle[b][a])

for i in diagonal1.copy():
    if len(i) < length:
        diagonal1.remove(i)
for i in diagonal2.copy():
    if len(i) < length:
        diagonal2.remove(i)
#
for diagonal in diagonal1:
    for i in range(len(diagonal)-length + 1):
        if word == diagonal[i:i+length] or word[::-1] == diagonal[i:i+length]:
            count += 1

for diagonal in diagonal2:
    for i in range(len(diagonal)-length + 1):
        if word == diagonal[i:i+length] or word[::-1] == diagonal[i:i+length]:
            count += 1
