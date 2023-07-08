# 15/15, don't forget to 'break'

count = int(input())
repeats = int(input())

times = []
count = 0

for _ in range(repeats):
    x = int(input())
    times.append(x)

times.sort()

for i in times:
    count -= i
    if count < 0:
        print(count)
        break

    count += 1

# other solution
# total_time = int(input())
# num_chores = int(input())
# chores = [int(input()) for _ in range(num_chores)]
# chores.sort()
#
# time_taken = 0
# chores_done = 0
# for chore in chores:
#     time_taken += chore
#     if time_taken > total_time:
#         break
#     else:
#         chores_done += 1
#
# print(chores_done)
