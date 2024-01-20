from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        upper_bound, lower_bound = len(nums) - 1, 0

        while lower_bound <= upper_bound:
            index = (upper_bound + lower_bound) // 2

            if target == nums[index]:
                return index 
            elif target > nums[index]:
                lower_bound = index + 1
            else:
                upper_bound = index - 1
        return lower_bound

    