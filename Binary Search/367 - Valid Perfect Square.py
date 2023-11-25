# Wouldnt work here because Leetcode has its own test cases
# To make it work, change the function according to you liking

# Declaring class
class Solution:
    #Declaring function
    def isPerfectSquare(self, num: int) -> bool:
        
        # To make sure the number is greater than 0
        if num < 0:
            return False

        # Assinging Variables
        left, right = 0, num

        # Start of loop
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1

        return False