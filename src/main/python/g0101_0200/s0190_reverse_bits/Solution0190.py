# #Easy #Top_Interview_Questions #Bit_Manipulation #Divide_and_Conquer
# #Algorithm_I_Day_14_Bit_Manipulation #Udemy_Bit_Manipulation #Top_Interview_150_Bit_Manipulation
# #2025_09_14_Time_36_ms_(75.17%)_Space_17.90_MB_(26.53%)

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        # because there are 32 bits in total
        for i in range(32):
            ret = ret << 1
            # If the bit is 1 we OR it with 1, ie add 1
            if (n & 1) > 0:
                ret = ret | 1
            n = n >> 1
        return ret
