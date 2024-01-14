from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        # Find the maximum frequency
        max_freq = max(count.values())

        # Count the number of elements with maximum frequency
        total_max_freq_elements = sum(freq for freq in count.values() if freq == max_freq)

        return total_max_freq_elements
