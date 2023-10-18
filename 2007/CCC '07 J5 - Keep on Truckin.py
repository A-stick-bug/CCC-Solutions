# simple DP
# O(m^2) where m is the number of motels
# dp[i] is the number of ways to get motel[i]
# minimum distance of a and maximum distance of b between 'jumps'

a = int(input())
b = int(input())
n = int(input())

motel = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]  # location of stops
motel.extend([int(input()) for _ in range(n)])  # add extra stops from input
motel.sort()

dp = [0] * (len(motel))
dp[0] = 1  # base case, there is always 1 way to get to the start

for i in range(len(motel)):  # for every motel i, find how many ways there are to get to it from motels before i
    for j in range(i):
        dist = motel[i] - motel[j]
        if a <= dist <= b:  # you can get to motel j from motel i
            dp[i] += dp[j]

print(dp[-1])
