# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Udemy_Arrays
# #Big_O_Time_O(n)_Space_O(n) #2025_07_24_Time_19_ms_(93.81%)_Space_34.68_MB_(19.66%)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter = 1
        nums = set(nums)
        while True:
            if counter not in nums:
                return counter
            counter += 1
