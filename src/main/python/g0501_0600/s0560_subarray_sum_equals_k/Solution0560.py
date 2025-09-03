# #Medium #Top_100_Liked_Questions #Array #Hash_Table #Prefix_Sum #Data_Structure_II_Day_5_Array
# #Big_O_Time_O(n)_Space_O(n) #2025_07_25_Time_27_ms_(84.54%)_Space_20.34_MB_(71.80%)

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        total, count = 0, 0

        for n in nums:
            total += n
            if total - k in sub_num:
                count += sub_num[total-k]
            sub_num[total] = 1 + sub_num.get(total, 0)
        
        return count
