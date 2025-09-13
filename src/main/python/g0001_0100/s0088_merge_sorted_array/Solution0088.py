# #Easy #Top_Interview_Questions #Array #Sorting #Two_Pointers #Data_Structure_I_Day_2_Array
# #Top_Interview_150_Array/String #2025_09_13_Time_0_ms_(100.00%)_Space_17.78_MB_(71.73%)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = len(nums1) - 1
        p2 = n - 1
        while p2 >= 0:
            if i >= 0 and nums1[i] > nums2[p2]:
                nums1[j] = nums1[i]
                j -= 1
                i -= 1
            else:
                nums1[j] = nums2[p2]
                j -= 1
                p2 -= 1
