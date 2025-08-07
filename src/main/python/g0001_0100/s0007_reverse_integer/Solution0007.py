# #Medium #Top_Interview_Questions #Math #Udemy_Integers #Big_O_Time_O(log10(x))_Space_O(1)
# #2025_07_22_Time_37_ms_(69.51%)_Space_17.70_MB_(57.22%)

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
