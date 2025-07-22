# #Hard #Top_100_Liked_Questions #String #Dynamic_Programming #Stack #Big_O_Time_O(n)_Space_O(1)
# #2025_07_22_Time_6_ms_(66.50%)_Space_17.80_MB_(97.72%)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        n = len(s)
        
        # First pass: left to right
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = 0
                right = 0
            if left == right:
                max_length = max(max_length, 2 * right)
        
        left = 0
        right = 0
        
        # Second pass: right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = 0
                right = 0
            if left == right:
                max_length = max(max_length, 2 * left)
        
        return max_length
