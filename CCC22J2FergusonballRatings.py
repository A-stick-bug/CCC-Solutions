repeats = int(input())

golds = 0
gold_team = True

i = 0

while repeats > i:
    points = int(input())
    foul = int(input())

    total = points * 5 - foul * 3

    if total > 40:
        golds += 1
    else:
        gold_team = False

    i += 1

print(golds, end="")

if gold_team == True:
    print("+")