# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Union_Find
# #Top_Interview_150_Hashmap #Big_O_Time_O(N_log_N)_Space_O(1)
# #2024_06_09_Time_338_ms_(82.56%)_Space_31.7_MB_(88.80%)

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
