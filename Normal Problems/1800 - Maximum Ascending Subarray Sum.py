class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int: #type:ignore

        cur_streak = maxi = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_streak += nums[i]
            else:
                cur_streak = nums[i]
            maxi = max(maxi, cur_streak)
        return maxi
