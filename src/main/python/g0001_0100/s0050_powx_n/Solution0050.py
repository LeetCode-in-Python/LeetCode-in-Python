# #Medium #Top_Interview_Questions #Math #Recursion #Udemy_Integers #Top_Interview_150_Math
# #2025_09_20_Time_0_ms_(100.00%)_Space_17.80_MB_(50.14%)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        res = 1.0
        if n < 0:
            nn = -nn
        while nn > 0:
            if nn % 2 == 1:
                nn -= 1
                res *= x
            else:
                x *= x
                nn //= 2
        if n < 0:
            return 1.0 / res
        return res
