class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  
            num = sum(int(digit) for digit in str(num))  
        return num

########################### Another smart one ############################################

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9