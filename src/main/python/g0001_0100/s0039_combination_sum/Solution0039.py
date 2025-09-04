# #Medium #Top_100_Liked_Questions #Array #Backtracking #Algorithm_II_Day_10_Recursion_Backtracking
# #Level_2_Day_20_Brute_Force/Backtracking #Udemy_Backtracking/Recursion
# #Top_Interview_150_Backtracking #Big_O_Time_O(2^n)_Space_O(n+2^n)
# #2025_07_22_Time_4_ms_(90.51%)_Space_17.64_MB_(98.10%)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub_list = []
        self.combinationSumRec(len(candidates), candidates, target, sub_list, ans)
        return ans

    def combinationSumRec(self, n: int, coins: List[int], amount: int, sub_list: List[int], ans: List[List[int]]):
        if amount == 0 or n == 0:
            if amount == 0:
                ans.append(sub_list.copy())
            return
        
        if amount - coins[n - 1] >= 0:
            sub_list.append(coins[n - 1])
            self.combinationSumRec(n, coins, amount - coins[n - 1], sub_list, ans)
            sub_list.pop()
        
        self.combinationSumRec(n - 1, coins, amount, sub_list, ans)
