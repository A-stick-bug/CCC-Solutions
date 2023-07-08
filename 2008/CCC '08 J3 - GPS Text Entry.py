def index_letter(letter,gps):
    for i in range(len(gps)):
        for j in range(len(gps[i])):
            if gps[i][j] == letter:
                return [i,j]


gps = [["A", "B", "C", "D", "E", "F"],
       ["G", "H", "I", "J", "K", "L"],
       ['M', 'N', 'O', 'P', 'Q', 'R'],
       ['S', 'T', 'U', 'V', 'W', 'X'],
       ['Y', 'Z', ' ', '-', '.', 'enter']]

letters = list(input())
letters.append('enter')

pointer = "A"
total = 0

for i in range(len(letters)):
    first = index_letter(pointer,gps)
    second = index_letter(letters[i], gps)
    total += abs(first[1] - second[1]) + abs(first[0] - second[0])
    pointer = letters[i]

print(total)