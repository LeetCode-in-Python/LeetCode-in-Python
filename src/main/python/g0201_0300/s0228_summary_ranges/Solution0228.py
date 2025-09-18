# #Easy #Array #Top_Interview_150_Intervals #2025_09_17_Time_0_ms_(100.00%)_Space_17.69_MB_(84.69%)

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges: List[str] = []
        if not nums:
            return ranges
        a = nums[0]
        b = a
        for i in range(1, len(nums)):
            if nums[i] != b + 1:
                if a == b:
                    ranges.append(str(a))
                else:
                    ranges.append(f"{a}->{b}")
                a = nums[i]
                b = a
            else:
                b += 1
        if a == b:
            ranges.append(str(a))
        else:
            ranges.append(f"{a}->{b}")
        return ranges
