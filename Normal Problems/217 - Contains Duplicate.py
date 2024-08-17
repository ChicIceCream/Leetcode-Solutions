from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type:ignore
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        for count in hashmap.values():
            if count > 1:
                return True
        
        return False
# -------------------------------------
# Faster version

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: #type:ignore
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            
        