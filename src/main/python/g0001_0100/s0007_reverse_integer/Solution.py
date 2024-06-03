# #Medium #Top_Interview_Questions #Math #Udemy_Integers
# #2024_06_03_Time_28_ms_(94.06%)_Space_16.5_MB_(93.17%)

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev > 2**31 - 1 or rev < -2**31:
            return 0

        return rev
