playlist = ["A", "B", "C", "D", "E"]

flag = True

while flag:
    cmd = input()
    repeats = int(input())
    for i in range(repeats):
        if cmd == "1":
            temp = playlist.pop(0)
            playlist.append(temp)
        elif cmd == "2":
            temp = playlist.pop()
            playlist.insert(0, temp)
        elif cmd == "3":
            playlist[0], playlist[1] = playlist[1], playlist[0]
        else:
            flag = False
            break

for i in playlist:
    print(i, end=" ")
