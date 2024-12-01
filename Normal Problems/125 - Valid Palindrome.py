class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False
        checking = ""

        for char in s:
            if char.isalnum():
                checking += char.lower()
        print(f"s : {s} and checking : {checking}")
        return checking == checking[::-1]


############################# Another Hard way #####################################

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1

        return True

    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
