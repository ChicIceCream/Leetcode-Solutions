class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return False

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared == x:
                return mid
                break
            elif squared < x:
                left = mid + 1
            else:
                right = mid - 1
        return right