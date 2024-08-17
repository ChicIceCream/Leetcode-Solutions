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
 