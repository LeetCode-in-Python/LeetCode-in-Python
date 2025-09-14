# #Medium #Top_Interview_Questions #Array #Dynamic_Programming #Greedy #Dynamic_Programming_I_Day_7
# #Udemy_Arrays #Top_Interview_150_Array/String
# #2025_09_14_Time_0_ms_(100.00%)_Space_18.77_MB_(70.67%)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
