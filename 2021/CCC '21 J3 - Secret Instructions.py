output = []

previous = ""

while True:
    code = str(input())

    if code == "99999":
        break

    x = list(code)

    if int(x[0]) + int(x[1]) == 0:
        output.append(f"{previous} {x[2]}{x[3]}{x[4]}")

    elif (int(x[0]) + int(x[1])) % 2 == 0:
        output.append(f"right {x[2]}{x[3]}{x[4]}")
        previous = "right"

    else:
        output.append(f"left {x[2]}{x[3]}{x[4]}")
        previous = "left"

for i in output:
    print(i)
