# #Medium #Array #Tree #Matrix #Divide_and_Conquer #Top_Interview_150_Divide_and_Conquer
# #2025_09_20_Time_79_ms_(99.05%)_Space_18.62_MB_(47.28%)

from typing import List, Optional

class Node:
    def __init__(self, val: bool = False, isLeaf: bool = False, 
                 topLeft: Optional['Node'] = None, topRight: Optional['Node'] = None,
                 bottomLeft: Optional['Node'] = None, bottomRight: Optional['Node'] = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    
    def __str__(self):
        if self.isLeaf:
            return f"[{int(self.val)},{int(self.isLeaf)}]"
        return f"[{int(self.val)},{int(self.isLeaf)}]{self.topLeft}{self.topRight}{self.bottomLeft}{self.bottomRight}"

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        n = len(grid)

        # Helper function for recursion
        def build(x, y, size):
            # Check if all values in this subgrid are same
            first_val = grid[x][y]
            is_same = True
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first_val:
                        is_same = False
                        break
                if not is_same:
                    break

            # Agar sab same hain -> Leaf Node
            if is_same:
                return Node(first_val == 1, True)

            # Otherwise -> divide into 4 parts
            half = size // 2
            return Node(
                True,  # val koi bhi ho, internal node ke liye irrelevant
                False, # Not a leaf
                topLeft=build(x, y, half),
                topRight=build(x, y + half, half),
                bottomLeft=build(x + half, y, half),
                bottomRight=build(x + half, y + half, half)
            )

        return build(0, 0, n)
