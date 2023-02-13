# 10/15 TLE

m = int(input())
n = int(input())

painting = [[0 for x in range(n)] for y in range(m)]
count = int(input())

for i in range(count):
    brush = input().split()
    if brush[0] == "R":  # increment all values in row by 1
        row = int(brush[1]) - 1
        painting[row] = list(map(lambda x: x + 1, painting[row]))

    elif brush[0] == "C":  # increment all values in column by 1
        col = int(brush[1]) - 1
        for x in range(len(painting)):
            painting[x][col] += 1

total = 0
for painting_row in painting:
    for tile in painting_row:
        if tile % 2 == 1:
            total += 1

print(total)