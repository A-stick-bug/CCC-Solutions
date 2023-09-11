from collections import Counter

books = input()
count = Counter(books)
ls = sl = ml = lm = sm = ms = 0

# count misplaced books
for i in range(count["L"]):
    if books[i] == "S":
        sl += 1
    elif books[i] == "M":
        ml += 1

for i in range(count["M"]):
    i += count["L"]
    if books[i] == "S":
        sm += 1
    elif books[i] == "L":
        lm += 1

for i in range(count["L"] + count["M"], len(books)):
    if books[i] == "L":
        ls += 1
    elif books[i] == "M":
        ms += 1

swaps = 0

# swap S and L
ls_swap = min(sl, ls)
swaps += ls_swap
sl, ls = sl - ls_swap, ls - ls_swap

# swap S and M
sm_swap = min(sm, ms)
swaps += sm_swap
sm, ms = sm - sm_swap, ms - sm_swap

# swap M and L
ml_swap = min(ml, lm)
swaps += ml_swap
ml, lm = ml - ml_swap, lm - ml_swap

# print(ls , sl , ml , lm , sm , ms)

# leftover swaps take 2 moves
slm = min(sl, lm, ms)
swaps += slm * 2
sl -= slm
lm -= slm
ms -= slm

sml = min(ls, ml, sm)
swaps += 2 * sml
ls -= slm
ml -= slm
sm -= slm

print(swaps)
