# #Easy #Top_100_Liked_Questions #Array #Binary_Search #Algorithm_I_Day_1_Binary_Search
# #Binary_Search_I_Day_2 #Top_Interview_150_Binary_Search #Big_O_Time_O(log_n)_Space_O(1)
# #2025_07_22_Time_0_ms_(100.00%)_Space_18.46_MB_(43.50%)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            guess = nums[mid]

            if(guess == target):
                return mid

            elif guess < target:
                low = mid + 1
                if nums[-1] == guess:
                    return mid + 1
                elif nums[low] > target:
                    return mid + 1              
            else: 
                high = mid - 1
                 
        return mid
