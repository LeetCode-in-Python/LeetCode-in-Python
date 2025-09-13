# #Easy #Top_Interview_Questions #Array #Math #Programming_Skills_II_Day_3 #Udemy_Arrays
# #Top_Interview_150_Math #2025_09_13_Time_0_ms_(100.00%)_Space_12.42_MB_(51.94%)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                sum_val = digits[i] + carry + num
            else:
                sum_val = digits[i] + carry
            carry = sum_val // 10
            digits[i] = sum_val % 10
        if carry != 0:
            ans = [0] * (len(digits) + 1)
            ans[0] = carry
            for i in range(1, len(ans)):
                ans[i] = digits[i - 1]
            return ans
        return digits
