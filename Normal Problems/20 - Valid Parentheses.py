class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        bracket_mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_mapping:
                if stack and stack[-1] == bracket_mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack