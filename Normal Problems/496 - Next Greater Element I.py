from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans=defaultdict(lambda : 0)
        stack=[]
        n = len(nums2)
        for i in reversed(range(n)):
            while(stack and nums2[i]>stack[-1]):
                stack.pop(-1)
            if stack:
                ans[nums2[i]] = stack[-1]
            else:
                ans[nums2[i]] = -1
            stack.append(nums2[i])
        stack.clear()
        for i in nums1:
            stack.append(ans[i])
        return stack
