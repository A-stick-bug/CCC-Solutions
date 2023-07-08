h = int(input())
time = int(input())

touch = "The balloon does not touch ground in the given time."

for t in range(1, time):
    altitude = -6*(t**4) + (h*t**3) + (2*t**2) + t

    if altitude <= 0:
        touch = f"The balloon first touches ground at hour:\n{t}"
        break

print(touch)