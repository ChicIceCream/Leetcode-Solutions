class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: #type:ignore
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

###################################### Another Solution ############################################
    # def removeElement(self, nums: List[int], val: int) -> int:
#         
#       nums[:] = [x for x in nums if x != val]

#         return len(nums)