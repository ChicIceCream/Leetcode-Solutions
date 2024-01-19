from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(1, rows):
            for col in range(cols):
                matrix[row][col] += min(
                    matrix[row - 1][max(col - 1, 0):col + 2]
                )

        return min(matrix[-1])


