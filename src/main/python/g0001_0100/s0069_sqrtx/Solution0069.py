# #Easy #Top_Interview_Questions #Math #Binary_Search #Binary_Search_I_Day_4
# #Top_Interview_150_Math #2025_09_20_Time_0_ms_(100.00%)_Space_17.75_MB_(51.52%)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
