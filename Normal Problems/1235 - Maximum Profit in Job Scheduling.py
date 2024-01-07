from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        max_profit = [0] * len(jobs)

        for i in range(len(jobs)):
            prev_non_overlapping = self.binary_search(jobs, i)
            current_profit = jobs[i][2] + (max_profit[prev_non_overlapping] if prev_non_overlapping != -1 else 0)
            max_profit[i] = max(current_profit, max_profit[i - 1] if i > 0 else 0)

        return max_profit[-1]

    def binary_search(self, jobs, current_index):
        low, high = 0, current_index - 1

        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[current_index][0]:
                if jobs[mid + 1][1] <= jobs[current_index][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1

        return -1
