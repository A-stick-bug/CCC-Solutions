from collections import deque

def check(state):  # helper function to check if all lights in current state can be turned off
    count = 0
    for light in state:
        if light:
            count += 1
        elif count < 4:
            return False
        else:
            count = 0
    return True

n = int(input())
lights = [int(input()) for _ in range(n)]

q = deque()
q.append(lights)
while q:
    state = q.popleft()
    for i in range(n):
        if not state[i]:
            state[i] = 1
            q.append(state)
