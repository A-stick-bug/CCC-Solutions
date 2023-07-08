l_count = 0
m_count = 0
misplaced_l = 0
misplaced_m = 0
m_in_l = 0
l_in_m = 0

shelf = input()

for i in range(len(shelf)):
    if shelf[i] == "L":
        l_count += 1
    elif shelf[i] == "M":
        m_count += 1

for i in range(0, l_count):
    if shelf[i] == "M":
        m_in_l += 1
        misplaced_l += 1
    elif shelf[i] == "S":
        misplaced_l += 1

for i in range(l_count, l_count + m_count):
    if shelf[i] == "L":
        l_in_m += 1
        misplaced_m += 1
    elif shelf[i] == "S":
        misplaced_m += 1

print(misplaced_l + misplaced_m - min(m_in_l, l_in_m))