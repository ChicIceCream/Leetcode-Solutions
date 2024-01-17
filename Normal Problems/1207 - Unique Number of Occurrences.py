from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        for num in arr:
            occurrences[num] += 1
        
        return len(set(occurrences.values())) == len(occurrences)
