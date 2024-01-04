from collections import Counter
from math import ceil
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0

        for num in counter.values():
            if num == 1:
                return -1
            ans += ceil(num / 3)
        return ans