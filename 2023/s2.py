# 15/15 solved in O(n^2)

x = int(input())
heights = input().split()
heights = list(map(int, heights))

vals = [float('inf') for _ in range(x + 1)]
vals[1] = 0  # asym value of length 1 is always 0

for i in range(0, x - 1):
    start, end = i, i + 1
    length = 2
    asym = 0

    while end < x and start >= 0:
        asym += abs(heights[end] - heights[start])
        vals[length] = min(asym, vals[length])
        end += 1
        start -= 1
        length += 2

for i in range(1, x - 1):
    start, end = i-1, i + 1
    length = 3
    asym = 0

    while end < x and start >= 0:
        asym += abs(heights[end] - heights[start])
        vals[length] = min(asym, vals[length])
        end += 1
        start -= 1
        length += 2

print(*vals[1:], sep=" ")
