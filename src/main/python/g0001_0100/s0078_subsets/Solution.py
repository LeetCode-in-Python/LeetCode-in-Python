# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Bit_Manipulation #Backtracking
# #Algorithm_II_Day_9_Recursion_Backtracking #Udemy_Backtracking/Recursion
# #Big_O_Time_O(2^n)_Space_O(n*2^n) #2024_06_09_Time_30_ms_(92.66%)_Space_16.7_MB_(74.16%)

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(n + 1):
            for subset in combinations(nums, i):
                res.append(list(subset))
        return res

# Example usage:
# sol = Solution()
# result = sol.subsets([1, 2, 3])
# print(result)  # Output should be [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
