# 15/15
# simple loops and if statement (dict is also recommended)
# question is slightly hard to understand

num = list(input())
n = len(num)
num = [int(num[i]) if i % 2 == 0 else num[i] for i in range(len(num))]  # convert to int

table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

total = table[num[-1]] * num[-2]  # last number is always added
for i in range(0, n - 2, 2):
    sign = 1
    if table[num[i + 1]] < table[num[i + 3]]:  # check if we are subtracting
        sign = -1

    total += table[num[i + 1]] * num[i] * sign

print(total)
