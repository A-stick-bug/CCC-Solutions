# 5 point question
current = int(input())

while True:
    current = int(current)
    current += 1
    if current <= 9:
        print(current)
        break

    elif 10 <= current <= 99:
        current = str(current)
        if current[0] != current[1]:
            print(current)
            break

    elif 100 <= current <= 999:
        current = str(current)
        if current[0] != current[1] and current[0] != current[2] and current[1] != current[2]:
            print(current)
            break

    elif 1000 <= current <= 9999:
        current = str(current)
        if current[0] != current[1] and current[0] != current[2] and current[0] != current[3] and current[1] != current[
            2] and current[1] != current[3] and current[2] != current[3]:
            print(current)
            break
    elif current >= 10000:
        current = str(current)
        if current[0] != current[1] and current[0] != current[2] and current[0] != current[3] and current[0] != current[
            4] and current[1] != current[2] and current[1] != current[3] and current[1] != current[4] and current[2] != \
                current[3] and current[2] != current[4] and current[3] != current[4]:
            print(current)
            break
