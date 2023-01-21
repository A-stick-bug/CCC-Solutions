limit = 15
s = "WELCOME TO CCC GOOD LUCK TODAY"

s_list = s.split()
length = [len(i) for i in s_list]  # length of letters

start, end = 0, 0
indexes = []
index = 0

# breaks on second loop
for i in range(2):
    start = end
    total = 0
    while total <= limit and index < len(s_list):
        if total + length[index] + 1 > limit:
            total += length[index]
        else:
            total += length[index] + 1
        index += 1

    end = index
    index -= 1

    if (index > len(s_list) and index == 5) or start == end:
        indexes.append([start, end+1])
    else:
        indexes.append([start, end-1])

print(indexes)
for i in indexes:
    print(s_list[i[0]:i[1]])


