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
