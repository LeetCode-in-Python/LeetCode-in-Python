# #Easy #Dynamic_Programming #Bit_Manipulation #LeetCode_75_Bit_Manipulation
# #Udemy_Bit_Manipulation #Big_O_Time_O(num)_Space_O(num)
# #2024_06_08_Time_55_ms_(88.80%)_Space_23_MB_(95.35%)

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
