# #Medium #Array #Bit_Manipulation #Top_Interview_150_Bit_Manipulation
# #2025_09_14_Time_0_ms_(100.00%)_Space_19.05_MB_(88.35%)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)
        return ones
