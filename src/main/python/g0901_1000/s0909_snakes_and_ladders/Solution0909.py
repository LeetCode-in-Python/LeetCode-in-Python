# #Medium #Array #Breadth_First_Search #Matrix #Top_Interview_150_Graph_BFS
# #2025_09_20_Time_15_ms_(89.20%)_Space_17.80_MB_(84.30%)

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = [False] * target
        queue = deque([1])
        visited[0] = True
        step = 0
        
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                current_label = queue.popleft()
                if current_label == target:
                    return step
                
                for next_label in range(current_label + 1, min(target + 1, current_label + 7)):
                    if visited[next_label - 1]:
                        continue
                    visited[next_label - 1] = True
                    
                    row, col = self.indexToPosition(next_label, n)
                    if board[row][col] == -1:
                        queue.append(next_label)
                    else:
                        queue.append(board[row][col])
            step += 1
        
        return -1
    
    def indexToPosition(self, index: int, n: int) -> tuple:
        vertical = n - 1 - (index - 1) // n
        if (n - vertical) % 2 == 1:
            horizontal = (index - 1) % n
        else:
            horizontal = n - 1 - (index - 1) % n
        return vertical, horizontal
