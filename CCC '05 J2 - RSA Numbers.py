def rsa_count(num, num2):
    total = 0

    for i in range(num,num2+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count == 4:
            total += 1

    return total


first = int(input())
second = int(input())

print(f"The number of RSA numbers between {first} and {second} is {rsa_count(first, second)}")
