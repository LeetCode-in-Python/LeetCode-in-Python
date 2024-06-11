207\. Course Schedule

Medium

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you **must** take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

*   For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]

**Output:** true

**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible. 

**Example 2:**

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]

**Output:** false

**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible. 

**Constraints:**

*   <code>1 <= numCourses <= 10<sup>5</sup></code>
*   `0 <= prerequisites.length <= 5000`
*   `prerequisites[i].length == 2`
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses</code>
*   All the pairs prerequisites[i] are **unique**.

To solve the Course Schedule problem, we can use a graph-based approach with topological sorting. We'll represent the courses and their prerequisites as a directed graph, and then perform a topological sort to determine if there exists any cycle in the graph. If there is a cycle, it means there is a dependency loop, and it won't be possible to complete all courses.

### Steps:

1. **Build the Graph**:
   - Create an adjacency list to represent the directed graph.
   - Iterate through the `prerequisites` array and add edges to the graph.

2. **Perform Topological Sorting**:
   - Implement a function for topological sorting, which can be done using Depth-First Search (DFS) or Breadth-First Search (BFS).
   - In each approach, keep track of the visited nodes and the current path.
   - If during DFS, we encounter a node that is already in the current path, it indicates a cycle, and we return False.
   - If the sorting completes without finding a cycle, return True.

3. **Check for Cycle**:
   - If any node has a cycle in its path, return False.

4. **Return Result**:
   - If no cycle is found, return True, indicating it's possible to finish all courses.

### Implementation:

```python
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Function for topological sorting using DFS
        def dfs(course, visited, path):
            if course in path:
                return False  # Cycle detected
            if visited[course]:
                return True  # Already visited
            visited[course] = True
            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor, visited, path):
                    return False
            path.remove(course)
            return True
        
        # Perform topological sorting for each course
        for course in range(numCourses):
            visited = [False] * numCourses
            path = set()
            if not dfs(course, visited, path):
                return False
        
        return True
```

### Explanation:

1. **Build the Graph**:
   - We use a defaultdict to create an adjacency list representation of the directed graph.
   - We iterate through the `prerequisites` array and add edges to the graph.

2. **Perform Topological Sorting**:
   - We implement a function `dfs` for topological sorting using Depth-First Search (DFS).
   - We keep track of visited nodes and the current path to detect cycles.
   - If we encounter a node that is already in the current path, it indicates a cycle, and we return False.
   - Otherwise, if DFS completes without finding a cycle, we return True.

3. **Check for Cycle**:
   - We iterate through each course and perform topological sorting.
   - If any node has a cycle in its path, we return False.

4. **Return Result**:
   - If no cycle is found, we return True, indicating it's possible to finish all courses.

This solution has a time complexity of O(V + E), where V is the number of courses and E is the number of prerequisites. The space complexity is O(V + E) for storing the graph.