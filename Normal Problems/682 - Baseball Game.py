stack = []
operations = ["5","2","C","D","+"]
for op in operations:
    if op.isdigit():
        stack.append(int(op))
        print(stack)
    elif op == '+':
        stack.append(op)
        print(stack)
        stack.append(stack[-1] + stack[-2])
    elif op == 'D':
        stack.append(stack[-1]**2)
        print(stack)
    elif op == 'C':
        stack.pop()
        print(stack)
