lines = int(input())

total_s = 0
total_t = 0

while lines > 0:
    words = input()
    list_words = list(words.lower())
    s = list_words.count("s")
    total_s += s

    t = list_words.count("t")
    total_t += t

    lines -= 1

if total_t > total_s:
    print("English")
else:
    print("French")
