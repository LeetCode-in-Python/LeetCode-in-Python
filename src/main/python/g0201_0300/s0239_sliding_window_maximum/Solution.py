# #Hard #Top_100_Liked_Questions #Array #Heap_Priority_Queue #Sliding_Window #Queue
# #Monotonic_Queue #Udemy_Arrays #Big_O_Time_O(n*k)_Space_O(n+k)
# #2025_07_25_Time_152_ms_(81.96%)_Space_30.79_MB_(96.65%)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for right in range(len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            if q[0] <= right - k:
                q.popleft()
            if right >= k - 1:
                result.append(nums[q[0]])
        return result
