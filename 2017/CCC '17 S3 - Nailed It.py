n = int(input())
arr = list(map(int, input().split()))

count = [0] * 2001  # frequency array
for i in arr:
    count[i] += 1

res = [0] * 4001  # res[i] is the length of fence with height i
for i in range(2001):
    for j in range(i, 2001):
        if i == j:
            res[i + j] += count[i] // 2
        else:
            res[i + j] += min(count[i], count[j])

max_length = max(res)
heights = res.count(max_length)
print(max_length, heights)
