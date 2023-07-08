def format_decimal(num):  # format decimal to exactly 2 decimal places
    num = str(round(num, 2))
    if num[-2] == ".":
        num += "0"
    return num


sheeps = []
eat = set()
for i in range(int(input())):
    sheeps.append((int(float(input()) * 10000), int(float(input()) * 10000)))

x = 0
while x <= 10000000:
    min_distance = float("inf")
    for sheep in sheeps:
        distance = (sheep[0] - x) ** 2 + sheep[1] ** 2
        if min_distance > distance:
            min_distance = distance
            min_sheeps = [sheep]
        elif min_distance == distance:
            min_sheeps.append(sheep)

    for i,j in min_sheeps:
        eat.add(f"({format_decimal(i / 10000)}, {format_decimal(j / 10000)})")
    x += 100

for i in eat:
    print(f"The sheep at {i} might be eaten.")
