# #Medium #Top_100_Liked_Questions #Array #Prefix_Sum #Data_Structure_II_Day_5_Array #Udemy_Arrays
# #Big_O_Time_O(n^2)_Space_O(n) #2024_06_09_Time_241_ms_(99.65%)_Space_25.5_MB_(94.18%)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [0] * len(nums)
        for num in nums:
            product *= num
        
        for i in range(len(nums)):
            if nums[i] != 0:
                ans[i] = product // nums[i]
            else:
                p = 1
                for j in range(len(nums)):
                    if j != i:
                        p *= nums[j]
                ans[i] = p
                
        return ans
