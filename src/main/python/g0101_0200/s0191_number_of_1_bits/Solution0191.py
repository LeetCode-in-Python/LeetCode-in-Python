# #Easy #Top_Interview_Questions #Bit_Manipulation #Algorithm_I_Day_13_Bit_Manipulation
# #Programming_Skills_I_Day_2_Operator #Udemy_Bit_Manipulation #Top_Interview_150_Bit_Manipulation
# #2025_09_14_Time_0_ms_(100.00%)_Space_17.66_MB_(81.24%)

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum_val = 0
        flag = False
        if n < 0:
            flag = True
            n = n - (1 << 31)  # Equivalent to Integer.MIN_VALUE
        while n > 0:
            k = n % 2
            sum_val += k
            n //= 2
        return sum_val + 1 if flag else sum_val
