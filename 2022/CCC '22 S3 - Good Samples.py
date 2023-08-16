import sys

n, m, k = map(int, input().split())
# assert n >= m  # for testing purposes

calc = lambda x: (x * (x + 1)) // 2
d = n - m
max_samples = calc(n) - calc(d)  # maximum number of good samples possible

if k > max_samples or k < n:
    print(-1)
    sys.exit()

k -= n
res = []
good = 0
for i in range(1, n + 1):
    k += 1  # add one by one because adding any number will increase the number of good samples by 1

    if good == k:  # already have the right amount of good samples
        res.append(res[-1])

    elif i <= m and good + i <= k:  # need more samples
        res.append(i)
        good += i

    elif i > m and good + m <= k:  # need more samples, max pitched reached, now cycling through 1 to m
        res.append(m if i % m == 0 else i % m)
        good += m  # when cycling through 1 to m, you get m new good samples for every note

    else:  # almost right
        diff = k - good
        res.append(res[-diff])

print(*res)

# # used for checking if the output is actually correct
#
# from collections import Counter
# def valid_sub(arr):  # could be optimized using sliding window but not worth the effort
#     res = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)+1):
#             sub = Counter(arr[i:j])
#             if all([v == 1 for v in sub.values()]):
#                 res += 1
#     return res
#
# ans = valid_sub(res)
# print(ans == k and max(res) <= m)  # answer is correct or not
# print(ans)
# print("----")
