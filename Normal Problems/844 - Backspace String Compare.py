class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char in s:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        
        for char in t:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        
        return stack_s == stack_t

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def pro(s):
            k = []
            for c in s:
                if c == '#':
                    if k:
                        k.pop()
                else:
                    k.append(c)
            return ''.join(k)
        
        return pro(s) == pro(t)