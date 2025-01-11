class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character to its numerical value and build a string
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)

        # Apply digit sum transformations k times
        for _ in range(k):
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            # Break early if the current number becomes less than 10
            if digit_sum < 10:
                return digit_sum
            numeric_string = str(digit_sum)

        # Convert the final string to integer and return
        return int(numeric_string)