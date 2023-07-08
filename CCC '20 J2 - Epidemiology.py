p = int(input())  # total
n = int(input())  # ppl with disease
r = int(input())  # spread multi
day = 0
count = 0
active = n

while n <= p:
    active = active * r
    n += active
    day += 1

print(day)
