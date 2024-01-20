from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        result = 0
        stack = []
        arr.append(0)  # Append a sentinel element to handle the last few elements in the array

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                result += arr[idx] * (i - idx) * (idx - stack[-1] if stack else idx + 1)
                result %= MOD
            stack.append(i)

        return result