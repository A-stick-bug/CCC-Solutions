# 15/15 optimizations possible

repeats = int(input())

to_print = []
letter = ""
count = 0

current = 0
while current < repeats:
    text = str(input())+"~"
    letter = text[0]

    for i in text:
        prev_letter = letter
        if letter == i:
            count += 1

        elif letter != i:
            to_print.append(f"{count} {prev_letter} ")
            letter = i
            count = 1

    #to_print.append(f"{count} {prev_letter} ")
    to_print.append("\n")
    current += 1
    letter = ""
    count = 0

for j in to_print:
    print(j,end="")
