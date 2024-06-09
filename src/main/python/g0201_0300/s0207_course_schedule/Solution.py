# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search
# #Breadth_First_Search #Graph #Topological_Sort #Big_O_Time_O(N)_Space_O(N)
# #2024_06_09_Time_86_ms_(76.64%)_Space_18.4_MB_(48.61%)

class Solution:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        colors = [self.WHITE] * numCourses
        
        for i in range(numCourses):
            if colors[i] == self.WHITE and adj[i] and self.hasCycle(adj, i, colors):
                return False
        return True

    def hasCycle(self, adj: List[List[int]], node: int, colors: List[int]) -> bool:
        colors[node] = self.GRAY
        
        for nei in adj[node]:
            if colors[nei] == self.GRAY:
                return True
            if colors[nei] == self.WHITE and self.hasCycle(adj, nei, colors):
                return True
        
        colors[node] = self.BLACK
        return False
