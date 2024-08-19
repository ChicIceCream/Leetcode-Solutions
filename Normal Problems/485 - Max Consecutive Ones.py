class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: #type:ignore
        max_consecutive_ones = 0
        current_consecutive_ones = 0

        for num in nums:
            if num == 1:
                current_consecutive_ones += 1
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
            else:
                current_consecutive_ones = 0

        return max_consecutive_ones