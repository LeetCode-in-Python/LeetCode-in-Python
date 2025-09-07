# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Union_Find
# #Top_Interview_150_Hashmap #Big_O_Time_O(N_log_N)_Space_O(1)
# #2025_07_25_Time_47_ms_(76.47%)_Space_33.24_MB_(81.27%)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1
                
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_length += 1
                
                max_length = max(max_length, cur_length)
        
        return max_length
