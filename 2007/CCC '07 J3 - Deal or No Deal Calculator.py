# 15/15 look at conditions for output more carefully

moneys = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
total = sum(moneys)

repeats = int(input())
count = 10 - repeats

i = 0
while i < repeats:
    amount = int(input())
    total -= moneys[amount-1]

    i += 1

offer = int(input())


if (total//count) > offer:
    print("no deal")
else:
    print("deal")
