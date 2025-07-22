# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Greedy #Two_Pointers
# #LeetCode_75_Two_Pointers #Algorithm_II_Day_4_Two_Pointers #Top_Interview_150_Two_Pointers
# #Big_O_Time_O(n)_Space_O(1) #2025_07_22_Time_68_ms_(91.16%)_Space_28.60_MB_(23.78%)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
        return max_area
