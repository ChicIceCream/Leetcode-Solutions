from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # freq should be a list of size nums + 1
        freq = [0] * (len(nums) + 1)
        ans = []

        for c in nums:

            if freq[c] >= len(ans):
                ans.append([])
                
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans