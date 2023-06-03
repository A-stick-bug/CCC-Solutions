import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


fib = [0,1]
num = 0
while num <= 10**15:
    num = fib[-1]+fib[-2]
    fib.append(num)
fib = set(fib)
fib.remove(1)  # 1 IS NOT COMPOSITE


for i in range(int(input())):
    x = int(input())
    if x in fib and not is_prime(x):
        print("YES")
    else:
        print("NO")

# you can basically just put these in a set and do if x in set
#0 8 21 34 55 144 377 610 987 2584 4181 6765 10946 17711 46368 75025 121393 196418 317811 832040 1346269 2178309 3524578 5702887 9227465
