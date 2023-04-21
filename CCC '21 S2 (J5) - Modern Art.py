from collections import defaultdict

ROWS = int(input())
COLS = int(input())
row_choice = defaultdict(int)
col_choice = defaultdict(int)
painting = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for i in range(int(input())):
    choice = input().split()
    if choice[0] == "R":
        row_choice[int(choice[1]) - 1] += 1
    else:
        col_choice[int(choice[1]) - 1] += 1

for row in row_choice.keys():
    if row_choice[row] % 2 == 1:
        painting[row] = list(map(lambda x: x + 1, painting[row]))

for col in col_choice.keys():
    if col_choice[col] % 2 == 1:
        for i in range(ROWS):
            painting[i][col] += 1


total = 0
for i in painting:
    for j in i:
        if j%2 ==1:
            total += 1
print(total)
