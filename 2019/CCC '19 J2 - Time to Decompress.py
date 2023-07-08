# 15/15 remember to cast to int

repeats = int(input())

to_print = []

i = 0
while i < repeats:
    decompress = input()
    decompress = decompress.split()

    to_print.append(int(decompress[0]) * decompress[1])

    i += 1

for j in to_print:
    print(j)