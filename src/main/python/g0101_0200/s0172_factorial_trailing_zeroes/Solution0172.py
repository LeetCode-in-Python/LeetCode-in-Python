# #Medium #Top_Interview_Questions #Math #Udemy_Integers #Top_Interview_150_Math
# #2025_09_14_Time_0_ms_(100.00%)_Space_17.76_MB_(53.50%)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        base = 5
        count = 0
        while n >= base:
            count += n // base
            base = base * 5
        return count
