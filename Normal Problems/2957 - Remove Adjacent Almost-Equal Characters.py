class Solution:
    def removeAlmostEqualCharacters(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 1
        
        while i < n:
            if abs(ord(s[i]) - ord(s[i - 1])) == 1 or s[i] == s[i - 1]:
                ans += 1
                i += 2
                continue
            i += 1
        
        return ans
