from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = binary_search_left(nums, target)
        right = binary_search_right(nums, target)

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]