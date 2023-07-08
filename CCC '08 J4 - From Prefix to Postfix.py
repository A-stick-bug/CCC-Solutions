# 15/15

def prefix_to_postfix(expression):
    stack = []
    operators = ['+', '-']
    expression = expression.split()
    for token in reversed(expression):
        if token in operators:
            val1 = stack.pop()
            val2 = stack.pop()
            # stack.append(f"({val1} {token} {val2})")  # for normal notation (infix)
            stack.append(f"({val1} {val2} {token})")  # remove parenthesis before submitting
        else:
            stack.append(token)
        # print(stack)  # to help understand how it works

    return stack[0]


line = input()
while line != "0":
    print(prefix_to_postfix(line))
    line = input()
