time = input().split(":")
time = list(map(int,time))

n = 120

while n > 0:
    # determine whether it is currently in rush hour traffic
    if 7 <= time[0] < 10 or 15 <= time[0] < 19:
        n -= 0.5
    else:
        n -= 1

    # increment time
    time[1] += 1
    if time[1] == 60:
        time[0] += 1
        time[1] = 0
        if time[0] == 24:
            time[0] = 0

if time[0] < 10:
    time[0] = "0" + str(time[0])
if time[1] < 10:
    time[1] = "0" + str(time[1])

print(f"{time[0]}:{time[1]}")