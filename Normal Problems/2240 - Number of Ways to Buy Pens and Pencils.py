class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        l = cost1 if cost1 > cost2 else cost2
        s = cost2 if l == cost1 else cost1
        
        res = 0
        maxl = total // l
        for n in range(maxl + 1):
            res += (total - n * l) // s + 1

        return res