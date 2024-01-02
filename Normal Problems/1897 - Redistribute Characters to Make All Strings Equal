from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # make a distionary to store all the values
        counts = defaultdict(int)
        
        # iterate through the words
        for word in words:
            
            #then the letters
            for c in word:
                counts[c] += 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True