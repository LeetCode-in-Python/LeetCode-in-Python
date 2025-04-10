# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Array #Dynamic_Programming #Two_Pointers
# #Stack #Monotonic_Stack #Dynamic_Programming_I_Day_9 #Udemy_Two_Pointers
# #Top_Interview_150_Array/String #Big_O_Time_O(n)_Space_O(1)
# #2024_06_08_Time_93_ms_(87.70%)_Space_18.5_MB_(68.72%)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        lower_wall = 0
        
        while l < r:
            l_val, r_val = height[l], height[r]
            if l_val < r_val:
                lower_wall = max(l_val, lower_wall)
                res += lower_wall - l_val
                l += 1
            else:
                lower_wall = max(r_val, lower_wall)
                res += lower_wall - r_val
                r -= 1
        
        return res
