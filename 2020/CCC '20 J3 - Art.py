# 15/15

items = int(input())

min_x = 100
max_x = 0
min_y = 100
max_y = 0

i = 0
while i < items:
    x = input()
    coords = x.split(",")
    if int(coords[0]) < min_x:
        min_x = int(coords[0])
    if int(coords[0]) > max_x:
        max_x = int(coords[0])
    if int(coords[1]) < min_y:
        min_y = int(coords[1])
    if int(coords[1]) > max_y:
        max_y = int(coords[1])

    i += 1

print(f"{min_x-1},{min_y-1}")
print(f"{max_x+1},{max_y+1}")


