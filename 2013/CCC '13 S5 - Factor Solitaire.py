"""
Greedy algorithm that works backwards
Literally came up with this solution from observing the explanation of sample output 2. (no idea why it works though)

Forwards: C=A*B, c += a, cost += b, end at input
Using this method is too slow because there are too many factors to consider

Backwards (starting from the input): C=A*B, c -= a, cost += b, end at 1
To minimize the cost when working backwards towards 1:
- we must use the largest factor of C as A (and the other factor B, will be the smallest)
- Note: we cannot use C as a factor of C because our goal is to reach 1, not 0

"""


def find_largest_factor(num):
    """Find the largest factor of num that != num"""
    for i in reversed(range(num // 2 + 1)):
        if num % i == 0:
            return i


n = int(input())
cost = 0

while n != 1:
    a = find_largest_factor(n)
    b = n // a  # n = a * b
    cost += b - 1  # have to minus one for some reason (again, not sure why)
    n -= a

print(cost)
