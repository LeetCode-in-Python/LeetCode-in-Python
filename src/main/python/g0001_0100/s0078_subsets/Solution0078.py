# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Bit_Manipulation #Backtracking
# #Algorithm_II_Day_9_Recursion_Backtracking #Udemy_Backtracking/Recursion
# #Big_O_Time_O(2^n)_Space_O(n*2^n) #2025_07_24_Time_0_ms_(100.00%)_Space_18.05_MB_(21.18%)

from itertools import combinations
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(n + 1):
            for subset in combinations(nums, i):
                res.append(list(subset))
        return res
