# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Two_Pointers #Bit_Manipulation
# #Binary_Search_II_Day_5 #Big_O_Time_O(n)_Space_O(n)
# #2024_06_08_Time_453_ms_(81.73%)_Space_31.1_MB_(24.78%)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)
        for num in nums:
            arr[num] += 1
            if arr[num] == 2:
                return num
        return 0
