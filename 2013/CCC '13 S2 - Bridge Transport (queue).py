"""
this is a cleaner and more efficient approach than my previous
note that because there are only 4 cars on the bridge, using a queue doesn't help much but theoretically,
it is much more efficient
"""

from collections import deque

limit = int(input())
n = int(input())
current = deque()
weight = count = 0

for _ in range(n):
    car = int(input())
    weight += car
    current.append(car)

    if len(current) > 4:
        weight -= current.popleft()
    if weight > limit:
        break
    else:
        count += 1
print(count)
