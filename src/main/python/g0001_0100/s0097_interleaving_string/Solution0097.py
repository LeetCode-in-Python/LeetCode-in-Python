# #Medium #String #Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #2025_09_13_Time_37_ms_(90.93%)_Space_18.18_MB_(44.68%)

from typing import List, Optional

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        cache: List[List[Optional[bool]]] = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        return self._isInterleave(s1, s2, s3, 0, 0, 0, cache)

    def _isInterleave(self, s1: str, s2: str, s3: str, i1: int, i2: int, i3: int, cache: List[List[Optional[bool]]]) -> bool:
        if cache[i1][i2] is not None:
            return cache[i1][i2]
        if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
            return True
        result = False
        if i1 < len(s1) and s1[i1] == s3[i3]:
            result = self._isInterleave(s1, s2, s3, i1 + 1, i2, i3 + 1, cache)
        if i2 < len(s2) and s2[i2] == s3[i3]:
            result = result or self._isInterleave(s1, s2, s3, i1, i2 + 1, i3 + 1, cache)
        cache[i1][i2] = result
        return result
