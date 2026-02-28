# https://dmoj.ca/problem/ccc26s3
# Part 1:
# What matters here is parity
# - If there are 2 even numbers, gcd>1
# - If there is 1 even and 2 odd, we can add the odds to make an even
# - If there are 4 odds, we can make 2 even pairs
# Notice that after taking care of these cases, the only one that remains is n <= 3, just brute force
#
# Part 2:
# Notice that the grader is not adaptive (i.e. the test case is fixed) and N is very big (10^5)
# Either the array has a lot of evens or it has a lot of odds
# Consider the strategy of picking 2 random (disjoint) pairs
# If there are many evens, chances are we will be able to pick (even,even) and (even,even)
# If there are many odds, chances are we will be able to pick (odd,odd) and (odd,odd)
# Since we have 100 guesses, the chances of being unlucky are astronomically low

from math import gcd

n = int(input())
arr = list(map(int, input().split()))


def solve1():
    odd = [i + 1 for i in range(n) if arr[i] % 2 == 1]
    even = [i + 1 for i in range(n) if arr[i] % 2 == 0]

    if len(even) >= 2:
        print("YES")
        print(1, 1)
        print(even[0])
        print(even[1])
    elif len(even) == 1 and len(odd) >= 2:
        print("YES")
        print(1, 2)
        print(even[0])
        print(odd[0], odd[1])
    elif len(even) == 0 and len(odd) >= 4:
        print("YES")
        print(2, 2)
        print(odd[0], odd[1])
        print(odd[2], odd[3])
    elif n == 2:
        if gcd(arr[0], arr[1]) > 1:
            print("YES")
            print(1, 1)
            print(1)
            print(2)
        else:
            print("NO")
    elif n == 3:
        f = 0
        for alice in range(3):
            other = [0, 1, 2]
            other.remove(alice)
            a, b = other
            if gcd(arr[alice], arr[a]) > 1:
                print("YES")
                print(1, 1)
                print(alice + 1)
                print(a + 1)
                f = 1
                break
            elif gcd(arr[alice], arr[b]) > 1:
                print("YES")
                print(1, 1)
                print(alice + 1)
                print(b + 1)
                f = 1
                break
            elif gcd(arr[alice], arr[a] + arr[b]) > 1:
                print("YES")
                print(1, 2)
                print(alice + 1)
                print(a + 1, b + 1)
                f = 1
                break
        if f == 0:
            print("NO")
    else:
        assert 0  # don't miss cases


if arr[0] == -1:
    from random import shuffle

    print(100)
    indices = list(range(1, n + 1))
    shuffle(indices)
    for i in range(100):
        a, b, c, d = [indices.pop() for _ in range(4)]  # pairs to get all parities
        print(2, 2)
        print(a, b)
        print(c, d)

else:
    solve1()
