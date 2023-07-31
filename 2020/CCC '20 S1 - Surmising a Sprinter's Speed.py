# 15/15
# sort measurements chronologically (increasing order)
# then check the speed for each consecutive pair of measurements

n = int(input())
measurements = [list(map(int, input().split())) for _ in range(n)]  # (time, location)
measurements.sort()  # sort based on time

max_speed = 0
for i in range(1, n):
    time = measurements[i][0] - measurements[i - 1][0]
    distance = abs(measurements[i][1] - measurements[i - 1][1])
    speed = distance / time
    max_speed = max(max_speed, speed)

print(max_speed)
