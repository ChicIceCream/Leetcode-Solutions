class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""  # Initialize an empty string to build the prefix
        
        for word in words:
            prefix += word  # Concatenate the current word to the prefix
            
            if prefix == s:  # Check if the prefix matches `s`
                return True
            elif len(prefix) > len(s):  # Stop early if the prefix exceeds `s`
                return False
        
        return False  # If the loop ends and no match is found
        