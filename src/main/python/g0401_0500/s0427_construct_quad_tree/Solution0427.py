# #Medium #Array #Tree #Matrix #Divide_and_Conquer #Top_Interview_150_Divide_and_Conquer
# #2025_09_20_Time_79_ms_(99.05%)_Space_18.62_MB_(47.28%)

from typing import List, Optional

class Node:
    def __init__(self, val: bool = False, is_leaf: bool = False,
                 top_left: Optional['Node'] = None, top_right: Optional['Node'] = None,
                 bottom_left: Optional['Node'] = None, bottom_right: Optional['Node'] = None):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
    
    def __str__(self):
        if self.is_leaf:
            return f"[{int(self.val)},{int(self.is_leaf)}]"
        return f"[{int(self.val)},{int(self.is_leaf)}]{self.top_left}{self.top_right}{self.bottom_left}{self.bottom_right}"

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
                top_left=build(x, y, half),
                top_right=build(x, y + half, half),
                bottom_left=build(x + half, y, half),
                bottom_right=build(x + half, y + half, half)
            )

        return build(0, 0, n)
