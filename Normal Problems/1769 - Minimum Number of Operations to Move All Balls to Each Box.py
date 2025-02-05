################################ BRUTE FORCE T_T ######################################

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        n = len(boxes)

        for i in range(n):
            moves = 0
            for j in range(n):
                if boxes[j] == '1':  
                    moves += abs(i - j)  
            answer.append(moves)

        return answer
