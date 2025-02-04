class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int: # type: ignore
        maxi = 1
        current_streak = 1
        back_streak = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current_streak += 1
                if maxi < current_streak:
                    maxi = current_streak
            else:
                current_streak = 1
            
            if nums[i] > nums[i + 1]:
                back_streak += 1
                if maxi < back_streak:
                    maxi = back_streak
            else:
                back_streak = 1
            #print(i, i+1, back_streak, maxi)
        return maxi