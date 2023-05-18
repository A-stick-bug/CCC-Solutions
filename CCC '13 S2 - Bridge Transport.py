# fairly straightforwards problem
# you can put the code inside a function and just use 'return' instead of the 'skip' variable

max_weight = int(input())
weights = [int(input()) for _ in range(int(input()))]

skip = False
current = 0
for i in range(4):  # in case less than 4 carts fit
    current += weights[i]
    if current > max_weight:
        print(i)
        skip = True
        break

# more than 4 carts fit so start removing carts
if not skip:
    for i in range(4,len(weights)):
        current += weights[i]
        current -= weights[i-4]
        if current > max_weight:
            print(i)
            skip = True
            break

    # the whole train fits
    if not skip:
        print(len(weights))
