class Solution:
    def calPoints(self, operations: List[str]) -> int: # type: ignore
        
        stack = []
        
        for op in operations:
            if op == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
            elif op == 'D':
                stack.append(int(stack[-1])*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        