def prefix_to_postfix(expression):
    stack = []
    operators = ['+', '-']
    expression = expression.split()
    for token in reversed(expression):
        if token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand1 + ' ' + operand2 + ' ' + token)
        else:
            stack.append(token)
    return stack[0]


line = input()
while line != "0":
    print(prefix_to_postfix(line))
    line = input()
