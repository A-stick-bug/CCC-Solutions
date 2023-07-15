# passes CCC cases but fails DMOJ ones due to TLE

def format_decimal(num):
    num = str(round(num, 2))
    if num[-2] == ".":
        num += "0"
    return num


sheeps = []
eat = set()
for i in range(int(input())):
    sheeps.append((int(float(input()) * 1000), int(float(input()) * 1000)))

x = 0
while x <= 1000000:
    min_distance = float("inf")
    for sheep in sheeps:
        distance = ((sheep[0] - x) ** 2 + sheep[1] ** 2)**0.5
        if min_distance > distance:
            min_distance = distance
            min_sheep = sheep

    eat.add(f"({format_decimal(min_sheep[0]/1000)}, {format_decimal(min_sheep[1]/1000)})")
    x += 10

for i in eat:
    print(f"The sheep at {i} might be eaten.")