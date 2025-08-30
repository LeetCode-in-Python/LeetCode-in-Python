# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Array #Stack #Monotonic_Stack
# #Big_O_Time_O(n_log_n)_Space_O(log_n) #2025_07_24_Time_63_ms_(99.53%)_Space_29.12_MB_(95.20%)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lefts = [0]
        best = 0
        heights.append(0)
        for i,h in enumerate(heights):
            if h > heights[lefts[-1]]:
                lefts.append(i)
            elif h == heights[lefts[-1]]:
                pass
            elif h < heights[lefts[-1]]:
                while lefts and h < heights[lefts[-1]]:
                    left = lefts.pop()
                    hh = heights[left]
                    ww = i - left
                    if hh * ww > best:
                        best = hh * ww
                lefts.append(left)
                heights[left] = h
        return best
