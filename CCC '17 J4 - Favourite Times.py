# 15/15, use % to reduce unnecessary run time

n = int(input())
time = [1, 2, 0, 0]
count = 0

# 31 special times in 720 minutes (1 full clock cycle)
if n > 720:
    count += (n // 720) * 31
    n %= 720

for i in range(n):
    # increment time
    time[3] += 1
    if time[3] > 9:
        time[3] = 0
        time[2] += 1
    if time[2] == 6 and time[3] == 0:
        time[2] = 0
        time[1] += 1
    if time[1] > 9:
        time[1] = 0
        time[0] += 1
    if time[0] == 1 and time[1] > 2:
        time = [0, 1, 0, 0]

    # print(time)

    # checking if special
    temp = time.copy()

    difference = temp[2] - temp[3]
    for j in range(len(temp) - 1):
        special = True
        if j == 0 and temp[j] == 0:
            continue
        if temp[j] - temp[j + 1] != difference:
            special = False
            break

    if special:
        count += 1
        special = False

print(count)
