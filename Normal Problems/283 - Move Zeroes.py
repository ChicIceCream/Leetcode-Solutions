class Solution:
    def moveZeroes(self, nums: List[int]) -> None: #type:ignore
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                # swap right and left elements
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # move the pointer 