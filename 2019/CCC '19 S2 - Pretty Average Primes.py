t = int(input())


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5+1)):
        if num % i == 0:
            return False
    return True


for i in range(t):
    num = int(input())
    # if num % 2 == 0:  # even number
    #     start, end = num - 1, num + 1
    # else:  # odd number
    #     start, end = num - 2, num + 2
    start = num - 1
    end = num + 1

    while is_prime(end) == False or is_prime(start) == False:
        start -= 1
        end += 1

    print(f"{start} {end}")