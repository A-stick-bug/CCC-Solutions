# python Counter is perfect for this question
from collections import Counter

n = int(input())
readings = [int(input()) for i in range(n)]
x = Counter(readings)
table = x.most_common()  # turn into a tuple with decreasing order


def find_greatest():
    first = table[0][0]
    highest_frequency = table[0][1]
    second_frequency = table[1][1]
    res = 0

    for num, frequency in table:
        if frequency != second_frequency and frequency != highest_frequency:
            return res
        else:
            res = max(res, abs(first - num))
    return res


print(find_greatest())
