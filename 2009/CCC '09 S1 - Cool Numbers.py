# for a number to be a square and a cube, we must be able to represent it in the form of X^6, where X is an integer
# there are so little 6th powers in the given range that we can just precompute them

power_6 = [1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441, 1000000, 1771561, 2985984, 4826809, 7529536,
           11390625, 16777216, 24137569, 34012224, 47045881, 64000000, 85766121, 113379904]

start = int(input())
end = int(input())

total = 0
for i in power_6:
    if start <= i <= end:
        total += 1
print(total)
