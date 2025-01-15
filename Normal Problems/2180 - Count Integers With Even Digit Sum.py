class Solution:
    def countEven(self, num: int) -> int:

        # initiate count to 0
        count = 0


        # iterate through all the number from 2 to num
        for num in range(2, num+1):

            cur_sum = 0
            cur_num = num

            while cur_num != 0:
                rem = cur_num % 10
                cur_sum += rem

                cur_num = cur_num // 10
            
            # compare if the current digit sum is even
            if cur_sum % 2 == 0:
                count += 1

        # return the total numbers that are having digit sum as a even number
        return count