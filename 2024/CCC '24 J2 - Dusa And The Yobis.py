current_size = int(input())

while True:
    size = int(input())
    if size >= current_size:
        print(current_size)
        break

    current_size += size
