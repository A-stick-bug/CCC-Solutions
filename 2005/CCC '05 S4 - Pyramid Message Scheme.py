# Tree data structure, basically just finding how many 'layers' it has
# that will be the maximum number of layers in the stack

for _ in range(int(input())):
    n = int(input())
    messages = [input() for _ in range(n)]
    stack = [messages[-1]]  # the last message will ALWAYS be to the root node of the tree
    res = 0

    for node in messages:
        if len(stack) > 1 and stack[-2] == node:  # message being sent back
            receiver = stack.pop()
            sender = stack[-1]

        else:  # sent message, waiting to receive
            stack.append(node)

        res = max(len(stack) - 1, res)  # minus one because for n connected nodes (in a line), there are n-1 edges
        # print(stack)
    
    # x2 because a message needs to be sent back and forth (double the time)
    print((n - res * 2) * 10)  # this is the time saved compared to old strategy (x10 as required by the question)
