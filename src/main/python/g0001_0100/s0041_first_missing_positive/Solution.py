# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Udemy_Arrays
# #Big_O_Time_O(n)_Space_O(n) #2024_06_08_Time_334_ms_(98.05%)_Space_34.7_MB_(28.20%)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter = 1
        nums = set(nums)
        while True:
            if counter not in nums:
                return counter
            counter += 1
