from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        sol = 0
        for i in range(len(nums)):#starting index of subarray
            for j in range(i + 1, len(nums)-1):
                if nums[j] - nums[j-1] != nums[j+1] - nums[j]:
                    break
                else:
                    sol += 1
        return sol