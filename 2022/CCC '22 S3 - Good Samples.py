# for these type of questions, solve the small cases by hand and look for patterns
# create a function for generating random cases and checking for correctness if needed (code for this at the bottom)
# ad-hoc, constructive, greedy algorithms

import sys

n, m, k = map(int, input().split())
# assert n >= m  # for testing purposes

calc = lambda x: (x * (x + 1)) // 2
d = n - m
max_samples = calc(n) - calc(d)  # maximum number of good samples possible

if k > max_samples or k < n:  # there are at least n good samples (all numbers are the same)
    print(-1)
    sys.exit()

k -= n
res = []
good = 0
for i in range(1, n + 1):
    k += 1  # add one by one because adding any number will increase the number of good samples by 1

    if good == k:  # already have the right amount of good samples
        res.append(res[-1])

    elif i <= m and good + i <= k:  # need more samples, add the number that gives the most extra samples
        res.append(i)
        good += i

    elif i > m and good + m <= k:  # need more samples, max pitch reached, now cycling through 1 to m
        res.append(m if i % m == 0 else i % m)
        good += m  # when cycling through 1 to m, you get m new good samples for every note

    else:  # almost right, instead of adding maximum samples, add just the right amount
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
