class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]  # convert the number into its binary form and slice off the '0b'
        
        complimented_num = [] # compliment the number
        for bit in binary_num:
            if bit == '1':
                complimented_num.append('0')
            else:
                complimented_num.append('1')
        
        # Convert the complemented binary string back to an integer
        complimented_num = "".join(complimented_num)
        return int(complimented_num, 2)