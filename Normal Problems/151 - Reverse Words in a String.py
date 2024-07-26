class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()

        return " ".join(array[::-1])