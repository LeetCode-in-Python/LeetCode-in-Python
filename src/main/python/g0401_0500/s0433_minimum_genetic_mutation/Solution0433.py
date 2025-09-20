# #Medium #String #Hash_Table #Breadth_First_Search #Graph_Theory_I_Day_12_Breadth_First_Search
# #Top_Interview_150_Graph_BFS #2025_09_20_Time_0_ms_(100.00%)_Space_17.66_MB_(47.68%)

from collections import deque
from typing import List, Set

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = deque([start])
        step = 0
        
        while queue:
            cur_size = len(queue)
            for _ in range(cur_size):
                cur = queue.popleft()
                if cur == end:
                    return step
                
                for next_mutation in self.getValidMutations(bank_set, cur):
                    queue.append(next_mutation)
                    bank_set.remove(next_mutation)
            step += 1
        
        return -1
    
    def getValidMutations(self, bank_set: Set[str], current: str) -> List[str]:
        valid_mutations = []
        for mutation in bank_set:
            diff = 0
            for i in range(len(mutation)):
                if mutation[i] != current[i]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                valid_mutations.append(mutation)
        return valid_mutations
