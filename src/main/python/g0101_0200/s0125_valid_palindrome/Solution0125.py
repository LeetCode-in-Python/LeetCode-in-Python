# #Hard #Array #Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #2025_09_14_Time_232_ms_(75.22%)_Space_28.79_MB_(85.10%)

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(re.findall('[A-Za-z0-9]+', s.lower()))
        return cleaned == cleaned[::-1]
