# 15/15 do not have to print all outputs at one, can print part by part

x = str(input())

letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
is_number = False
number_to_print = 0

for i in x:
    if i in numbers:
        is_number = True
        print(i, end="")

    elif i not in numbers:
        if is_number:
            print()
            is_number = False

        if i == "+":
            print(" tighten ", end="")
            is_number = False

        elif i == "-":
            print(" loosen ", end="")
            is_number = False

        elif i in letters:
            print(i, end="")
            is_number = False
