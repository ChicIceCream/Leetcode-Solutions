class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        open_count = 0
        
        for char in s:
            if char == '(':
                if open_count > 0:  # If this is not the outermost '(', add it to the result
                    result.append(char)
                open_count += 1
            elif char == ')':
                open_count -= 1
                if open_count > 0:  # If this is not the outermost ')', add it to the result
                    result.append(char)
        
        return ''.join(result)
