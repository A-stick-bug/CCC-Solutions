fences = int(input())
heights = input().split()
base = input().split()
heights = list(map(int, heights))
base = list(map(int, base))

b = 0
h = 0

total = 0
for i in range(fences):
    area = (0.5 * base[b] * (heights[h] + heights[h + 1]))
    b += 1
    h += 1

    #print(area)
    total += area

print(total)
