# counting sort problem since the max length of each piece of wood is only 2000
# more about counting sort here: https://www.geeksforgeeks.org/counting-sort/

n = int(input())
boards = list(map(int, input().split()))

# how many times each length appears
length = [0] * 2001
for board in boards:
    length[board] += 1

# possible heights of 2 boards together
heights = [0] * 4001

for i in range(2000):
    for j in range(i, 2000):
        if i == j:
            heights[i + j] += length[i] // 2
        else:
            heights[i + j] += min(length[i], length[j])

longest = max(heights)
count = heights.count(longest)
print(longest, count)
