class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            # x is the first number and y is the second number
            y = target - nums[x]
            if y in hashmap:
                return [x, hashmap[y]]
            hashmap[nums[x]] = x