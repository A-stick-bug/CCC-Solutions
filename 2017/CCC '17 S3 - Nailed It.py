n = int(input())
boards = list(map(int, input().split()))

# how many times each length appears
length = [0] * 2001
for board in boards:
    length[board] += 1

combinations = [0] * 4001

for i in range(2000):
    for j in range(i, 2001):
        if i == j:
            combinations[i + j] += length[i] // 2
        else:
            combinations[i + j] += min(length[i], length[j])

longest = max(combinations)
count = combinations.count(longest)
print(longest, count)
