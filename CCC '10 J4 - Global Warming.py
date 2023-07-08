"""
How the code works:
First extract the sequence from the temperatures
Test the following for every sequence length, starting from shortest and break when a working sequence is found
(guarantees the found sequence to be shortest):
    remove all occurrences of the sequence in the array
    to test if the sequence works, check if the remaining part after removing all
    instances of the sequence is the start of the sequence

Note: the flag variable is for in case there is no shorter sequence
"""

x = input().split()
while x != ["0"]:
    x = list(map(int, x))

    length = x[0]
    temps = x[1:]
    sequence = []
    # extract sequence
    for i in range(len(temps) - 1):
        sequence.append(temps[i + 1] - temps[i])

    # in case the shortest sequence is the sequence itself
    flag = False

    for i in range(1, len(sequence)):
        test = True
        sub = sequence[:i]
        temp = sequence.copy()
        while len(temp) > len(sub):  # could just manipulate indices instead of deleting part of lsit every time
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