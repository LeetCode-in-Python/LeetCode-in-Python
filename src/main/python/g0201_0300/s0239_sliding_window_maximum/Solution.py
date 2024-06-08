# #Hard #Top_100_Liked_Questions #Array #Heap_Priority_Queue #Sliding_Window #Queue
# #Monotonic_Queue #Udemy_Arrays #Big_O_Time_O(n*k)_Space_O(n+k)
# #2024_06_08_Time_1093_ms_(66.83%)_Space_32_MB_(94.89%)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0] * (n - k + 1)
        dq = deque()
        i, j = 0, 0
        x = 0
        
        while j < len(nums):
            while dq and dq[-1] < nums[j]:
                dq.pop()
            dq.append(nums[j])
            
            if j - i + 1 == k:
                res[x] = dq[0]
                x += 1
                if dq[0] == nums[i]:
                    dq.popleft()
                i += 1
            j += 1
        
        return res
