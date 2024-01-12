from collections import defaultdict

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels_dict = defaultdict(int)

        for vowel in vowels:
            vowels_dict[vowel] = 0

        def count_vowels(string):
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid = length // 2

        a = s[:mid]
        b = s[mid:]

        return count_vowels(a) == count_vowels(b)