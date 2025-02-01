class Solution(object):
    def sumOfThree(self, num: int) -> List[int]: #type:ignore
        if num % 3 == 0:
            num //= 3
            return [num - 1, num, num + 1]
        return []