times = {}
waiting = set()
total_time = [0] * 101
time = 0

for _ in range(int(input())):
    entry, name = input().split()
    name = int(name)

    if entry == 'R':
        times[name] = time
        waiting.add(name)

    elif entry == 'S':
        total_time[name] += time - times[name]
        waiting.remove(name)

    else:
        time += name - 2
    time += 1

for name, wait in enumerate(total_time):
    if wait != 0 or name in waiting:
        if name in waiting:
            print(name, -1)
        else:
            print(name, wait)

