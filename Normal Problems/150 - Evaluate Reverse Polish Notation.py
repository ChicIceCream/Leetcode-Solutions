class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []    
        
        for char in tokens:
            if char == '+' or char == '-' or char =='*' or char == '/':
                if stack:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if char == '+':
                        stack.append(a + b)
                    elif char == '-':
                        stack.append(b - a)
                    elif char == '*':
                        stack.append(a * b)
                    else:
                        stack.append(int(b / a))
            else:
                stack.append(char)

        if stack:
            return int(round(float(''.join(map(str, stack)))))
        else: 
            return 0