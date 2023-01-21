# easy

text = input()
to_find = list(input())
printing = "no"

for _ in range(len(to_find)):
    temp = to_find[0]
    del to_find[0]
    to_find.append(temp)

    to_find_string = ''.join(to_find)

    if to_find_string in text:
        printing = "yes"
        break

print(printing)