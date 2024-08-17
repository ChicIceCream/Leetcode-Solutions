class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]: #type:ignore
        results = []
    
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            
            if subarray == sorted(subarray):
                if all(subarray[j] + 1 == subarray[j + 1] for j in range(k - 1)):
                    results.append(max(subarray)) # to get the max
                else:
                    results.append(-1)
            else:
                results.append(-1)
        
        return results