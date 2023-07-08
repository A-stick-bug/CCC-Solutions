times = int(input())

highest = ""
highest_number = 0

time = 0
while time < times:
    name = input()
    amount = int(input())

    if amount > highest_number:
        highest = name
        highest_number = amount

    time += 1

print(highest)