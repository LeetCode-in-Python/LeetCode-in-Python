# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Binary_Search
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_11 #Level_2_Day_8_Binary_Search
# #Udemy_Binary_Search #Top_Interview_150_Binary_Search #Big_O_Time_O(log_n)_Space_O(1)
# #2024_06_08_Time_36_ms_(91.71%)_Space_16.8_MB_(98.65%)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                return mid
            # If the left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # If the right half is sorted
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1
