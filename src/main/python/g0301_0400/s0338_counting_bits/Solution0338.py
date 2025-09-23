# #Easy #Dynamic_Programming #Bit_Manipulation #LeetCode_75_Bit_Manipulation
# #Udemy_Bit_Manipulation #Big_O_Time_O(num)_Space_O(num)
# #2025_07_25_Time_3_ms_(94.51%)_Space_18.68_MB_(22.83%)

from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        borderPos = 1
        incrPos = 1
        
        for i in range(1, len(result)):
            if incrPos == borderPos:
                result[i] = 1
                incrPos = 1
                borderPos = i
            else:
                result[i] = 1 + result[incrPos]
                incrPos += 1
                
        return result
