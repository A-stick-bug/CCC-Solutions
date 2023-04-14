input1 = input()
stack = []
while input1 != "SCHOOL":
    stack.append(input1)
    input1 = input()

home_direction = "LEFT" if stack.pop(0) == "R" else "RIGHT"

while stack:
    direction = stack.pop()
    current = stack.pop()
    if direction == "R":
        direction = "LEFT"
    else:
        direction = "RIGHT"
    print(f"Turn {direction} onto {current} street.")
print(f"Turn {home_direction} into your HOME.")

