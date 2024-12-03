class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int: #type:ignore
        # set prefix length to iterate the word
        prefix_len = len(pref)
        counter = 0 

        for i in range(len(words)):
            if pref == words[i][:prefix_len]:
                counter += 1
        
        return counter
            
        