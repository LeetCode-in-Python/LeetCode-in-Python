# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Greedy #Two_Pointers
# #LeetCode_75_Two_Pointers #Algorithm_II_Day_4_Two_Pointers #Top_Interview_150_Two_Pointers
# #Big_O_Time_O(n)_Space_O(1) #2024_06_04_Time_488_ms_(91.81%)_Space_29.5_MB_(60.76%)

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
