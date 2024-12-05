class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        
        for prefix in words:
            # get the len of every prefix because their lengths differ
            lenPrefix = len(prefix)
            if prefix == s[:lenPrefix]:
                counter += 1
        
        return counter
    
    