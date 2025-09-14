# #Medium #Top_Interview_Questions #Depth_First_Search #Breadth_First_Search #Graph
# #Topological_Sort #Level_2_Day_11_Graph/BFS/DFS #Top_Interview_150_Graph_General
# #2025_09_14_Time_0_ms_(100.00%)_Space_19.28_MB_(48.32%)

from typing import List, Dict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for classes in prerequisites:
            graph[classes[0]].append(classes[1])
        output = []
        visited = {}
        for c in graph.keys():
            if self._dfs(c, graph, visited, output):
                return []
        return output

    def _dfs(self, course: int, graph: Dict[int, List[int]], 
             visited: Dict[int, bool], output: List[int]) -> bool:
        if course in visited:
            return visited[course]
        visited[course] = True
        for c in graph[course]:
            if self._dfs(c, graph, visited, output):
                return True
        visited[course] = False
        output.append(course)
        return False
