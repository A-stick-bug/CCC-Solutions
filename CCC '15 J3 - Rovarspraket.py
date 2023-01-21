# 15/15 watch out for indexing [1:3] indexes 1, 2, and not 3

text = input()

alphabet = "abcdefghijklmnopqrstuvwxyzzz"
vowels = "aeiou"
index = 0
to_print = []
second = ""

for i in text:
    if i in vowels:
        to_print.append(i)
    else:
        index = alphabet.find(i)
        to_print.append(alphabet[index])

        if i in alphabet[1:3]:
            to_print.append("a")

        elif i in alphabet[3:7]:
            to_print.append("e")

        elif i in alphabet[7:12]:
            to_print.append("i")

        elif i in alphabet[12:18]:
            to_print.append("o")

        else:
            to_print.append("u")

        if alphabet[index + 1] in vowels:
            to_print.append(alphabet[index + 2])
        else:
            to_print.append(alphabet[index + 1])

for j in to_print:
    print(j, end="")
