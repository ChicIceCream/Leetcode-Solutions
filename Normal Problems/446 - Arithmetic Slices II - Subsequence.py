class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        count = 0
        dp = [{} for _ in range(n)] 

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
                    count += dp[j][diff] 
                dp[i][diff] = dp[i].get(diff, 0) + 1

        return count