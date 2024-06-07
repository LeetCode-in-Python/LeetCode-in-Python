# #Medium #Top_100_Liked_Questions #Array #Hash_Table #Prefix_Sum #Data_Structure_II_Day_5_Array
# #Big_O_Time_O(n)_Space_O(n) #2024_06_07_Time_224_ms_(72.29%)_Space_19.4_MB_(91.64%)

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tempSum = 0
        ret = 0
        sumCount = defaultdict(int)
        sumCount[0] = 1
        
        for i in nums:
            tempSum += i
            if tempSum - k in sumCount:
                ret += sumCount[tempSum - k]
            sumCount[tempSum] += 1
        
        return ret
