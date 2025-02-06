
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)

        for i in s1:
            hash1[i] += 1
        for i in s2:
            hash2[i] += 1

        if hash1 != hash2:
            return False
        if s1 == s2:
            return True

        index_to_change = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index_to_change.append(i)
        
        if len(index_to_change) == 2:
            i, j = index_to_change
            return s1[i] == s2[j] and s1[j] == s2[i]
        return False
