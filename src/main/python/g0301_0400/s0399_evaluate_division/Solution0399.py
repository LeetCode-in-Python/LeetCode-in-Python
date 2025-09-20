# #Medium #Array #Depth_First_Search #Breadth_First_Search #Graph #Union_Find #Shortest_Path
# #LeetCode_75_Graphs/DFS #Top_Interview_150_Graph_General
# #2025_09_20_Time_0_ms_(100.00%)_Space_17.82_MB_(72.87%)

from typing import Dict, List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.root: Dict[str, str] = {}
        self.rate: Dict[str, float] = {}
        
        # Initialize all variables
        for equation in equations:
            x, y = equation[0], equation[1]
            self.root[x] = x
            self.root[y] = y
            self.rate[x] = 1.0
            self.rate[y] = 1.0
        
        # Union all equations
        for i, equation in enumerate(equations):
            x, y = equation[0], equation[1]
            self.union(x, y, values[i])
        
        # Process queries
        result = []
        for query in queries:
            x, y = query[0], query[1]
            if x not in self.root or y not in self.root:
                result.append(-1.0)
                continue
            
            root_x = self.findRoot(x, x, 1.0)
            root_y = self.findRoot(y, y, 1.0)
            
            if root_x == root_y:
                result.append(self.rate[x] / self.rate[y])
            else:
                result.append(-1.0)
        
        return result
    
    def union(self, x: str, y: str, v: float) -> None:
        root_x = self.findRoot(x, x, 1.0)
        root_y = self.findRoot(y, y, 1.0)
        self.root[root_x] = root_y
        r1 = self.rate[x]
        r2 = self.rate[y]
        self.rate[root_x] = v * r2 / r1
    
    def findRoot(self, original_x: str, x: str, r: float) -> str:
        if self.root[x] == x:
            self.root[original_x] = x
            self.rate[original_x] = r * self.rate[x]
            return x
        return self.findRoot(original_x, self.root[x], r * self.rate[x])
