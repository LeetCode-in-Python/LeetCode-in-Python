# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Binary_Search
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_5 #Top_Interview_150_Binary_Search
# #Big_O_Time_O(log_n)_Space_O(1) #2025_07_22_Time_0_ms_(100.00%)_Space_18.99_MB_(75.63%)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        ans[0] = self.helper(nums, target, False)
        ans[1] = self.helper(nums, target, True)
        return ans

    def helper(self, nums: List[int], target: int, equals: bool) -> int:
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                result = mid
            if nums[mid] < target or (nums[mid] == target and equals):
                l = mid + 1
            else:
                r = mid - 1
        return result
