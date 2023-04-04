for _ in range(int(input())):
    max_num = int(input())
    current = 1
    arr = []
    stack = []
    for _ in range(max_num):
        arr.append(int(input()))
    for _ in range(max_num):
        car = arr.pop()
        if car == current:
            current += 1
            while stack and stack[-1] == current:
                stack.pop()
                current += 1
        else:
            stack.append(car)
    if not stack:
        print("Y")
    else:
        print("N")