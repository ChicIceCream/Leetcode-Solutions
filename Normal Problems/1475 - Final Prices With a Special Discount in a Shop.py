from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = prices[:]  # Start with a copy of prices as the answer list
        
        for i in range(len(prices)):
            # Apply the discount from the first lower or equal price to the right
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                answer[index] -= prices[i]
            stack.append(i)
        
        return answer
