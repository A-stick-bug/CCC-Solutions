total_time = int(input())
num_chores = int(input())
chores = [int(input()) for _ in range(num_chores)]
chores.sort()

time_taken = 0
chores_done = 0
for chore in chores:
    time_taken += chore
    if time_taken > total_time:
        break
    else:
        chores_done += 1

print(chores_done)
