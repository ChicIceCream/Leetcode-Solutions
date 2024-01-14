from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = Counter(word1)
        set2 = Counter(word2)

        if set1.keys() != set2.keys():
            return False 

        return sorted(list(set1.values())) == sorted(list(set2.values()))