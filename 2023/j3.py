days = int(input())

db = []

for i in range(days):
    people = list(input())
    db.append(people)

db = list(zip(*db))
yeses = []

for i in range(len(db)):
    yes = db[i].count("Y")
    yeses.append(yes)

most = max(yeses)
out = []

for i, day in enumerate(yeses,start=1):
    if day == most:
        out.append(i)

for i in range(len(out)-1):
    print(out[i],end=",")

print(out[-1],end="")
