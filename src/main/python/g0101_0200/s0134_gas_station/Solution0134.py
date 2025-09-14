# #Medium #Top_Interview_Questions #Array #Greedy #Top_Interview_150_Array/String
# #2025_09_14_Time_15_ms_(88.80%)_Space_23.18_MB_(96.18%)

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = sum(gas), sum(cost)
        if total_gas < total_cost:
            return -1  # impossible
        
        start, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1  # reset starting point
                tank = 0
        return start
