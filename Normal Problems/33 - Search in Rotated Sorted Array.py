from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Declaring variables
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 
            
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1