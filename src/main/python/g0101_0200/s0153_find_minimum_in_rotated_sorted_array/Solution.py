# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Algorithm_II_Day_2_Binary_Search
# #Binary_Search_I_Day_12 #Udemy_Binary_Search #Top_Interview_150_Binary_Search
# #Big_O_Time_O(log_N)_Space_O(log_N) #2025_07_25_Time_0_ms_(100.00%)_Space_18.07_MB_(50.37%)

class Solution:
    def findMinUtil(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return nums[l]
        
        mid = (l + r) // 2
        
        if mid == l and nums[mid] < nums[r]:
            return nums[l]
        
        if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        
        if nums[mid] < nums[l]:
            return self.findMinUtil(nums, l, mid - 1)
        elif nums[mid] > nums[r]:
            return self.findMinUtil(nums, mid + 1, r)
        
        return self.findMinUtil(nums, l, mid - 1)

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        return self.findMinUtil(nums, l, r)
