# #Medium #Array #Binary_Search #Prefix_Sum #Sliding_Window #Algorithm_II_Day_5_Sliding_Window
# #Binary_Search_II_Day_1 #Top_Interview_150_Sliding_Window
# #2025_09_14_Time_7_ms_(91.69%)_Space_28.40_MB_(10.62%)

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_res=float('inf')
        n=len(nums)
        l=0
        r=0
        curr=0
        while r<n:
           
            curr+=nums[r]
            while curr>=target:
                curr-=nums[l]
                min_res=min(min_res,r-l+1)
                l+=1
            r+=1    

            
        return min_res if min_res!=float('inf') else 0
