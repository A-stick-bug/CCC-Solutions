x = input().split()
while x != ["0"]:
    x = list(map(int, x))

    length = x[0]
    temps = x[1:]
    sequence = []
    for i in range(len(temps) - 1):
        sequence.append(temps[i + 1] - temps[i])

    # in case the shortest sequence is the sequence itself
    flag = False

    for i in range(1, len(sequence)):
        test = True
        sub = sequence[:i]
        temp = sequence.copy()
        while len(temp) > len(sub):
            if temp[:i] == sub:
                del temp[:i]
            else:
                test = False
                break
        if test:
            if temp == sequence[:len(temp)]:
                print(i)
                flag = True
                break
    if not flag:
        print(len(sequence))
    x = input().split()
