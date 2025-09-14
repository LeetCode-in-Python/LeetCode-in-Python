# #Hard #Array #Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #2025_09_14_Time_232_ms_(75.22%)_Space_28.79_MB_(85.10%)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        fb = float('-inf')  # first buy
        sb = float('-inf')  # second buy
        fs = 0  # first sell
        ss = 0  # second sell
        for price in prices:
            fb = max(fb, -price)
            fs = max(fs, fb + price)
            sb = max(sb, fs - price)
            ss = max(ss, sb + price)
        return ss
