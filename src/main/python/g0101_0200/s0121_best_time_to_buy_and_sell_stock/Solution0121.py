# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Dynamic_Programming
# #Data_Structure_I_Day_3_Array #Dynamic_Programming_I_Day_7 #Level_1_Day_5_Greedy #Udemy_Arrays
# #Top_Interview_150_Array/String #Big_O_Time_O(N)_Space_O(1)
# #2025_07_25_Time_17_ms_(98.03%)_Space_26.89_MB_(77.51%)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
