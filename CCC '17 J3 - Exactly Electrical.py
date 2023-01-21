x = input()
y = input()
charge = int(input())

x = x.split()
y = y.split()

x1 = int(x[0])
y1 = int(y[0])
x2 = int(x[1])
y2 = int(y[1])

run = x1 - y1
rise = x2 - y2

if str(run)[0] == "-":
    run = str(run)
    run = run.replace("-", "")
    run = int(run)

if str(rise)[0] == "-":
    rise = str(rise)
    rise = rise.replace("-", "")
    rise = int(rise)

total = rise + run

if (charge%2 == total%2) and charge >= total:
    print("Y")
else:
    print("N")
