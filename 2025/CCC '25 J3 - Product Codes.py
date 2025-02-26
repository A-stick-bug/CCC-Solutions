# https://dmoj.ca/problem/ccc25j3
# Implementation problem with some simple math

def solve():
    s = input()
    res = []
    total_num = 0
    cur_num = 0
    is_negative = False

    for char in s:
        if char.isnumeric():
            cur_num = 10 * cur_num + int(char)
        else:
            if is_negative:
                cur_num *= -1
            total_num += cur_num
            cur_num = 0
            is_negative = False

            if char == "-":
                is_negative = True
            elif char.islower():  # lowercase
                continue
            else:  # uppercase
                res.append(char)

    if is_negative:
        cur_num *= -1
    total_num += cur_num

    print("".join(res) + str(total_num))


t = int(input())
for _ in range(t):
    solve()

"""
3
Ahkiy-6ebvXCV1
393hhhUHkbs5gh6QpS-9-8
PL12N-2G1234Duytrty8-86tyaYySsDdEe
 """
