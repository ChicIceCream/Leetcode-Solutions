stack = []

operations = ["5","-2","4","C","D","9","+","+"]

for op in operations:
    if op == '+':
        print(stack)
        stack.append(int(stack[-2]) + int(stack[-1]))
    elif op == 'D':
        stack.append(int(stack[-1])*2)
        print(stack)
    elif op == 'C':
        stack.pop()
        print(stack)
    else:
        stack.append(int(op))
        print(stack)