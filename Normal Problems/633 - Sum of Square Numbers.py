import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
        left, right = a, b
        
        while left <= right:
            current_sum = left**2 + right**2
            
            if current_sum == c:
                return True
            elif current_sum > c:
                right -= 1
            else:
                left += 1
        
        return False