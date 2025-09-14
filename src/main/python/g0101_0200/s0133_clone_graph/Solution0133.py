# #Medium #Hash_Table #Depth_First_Search #Breadth_First_Search #Graph #Udemy_Graph
# #Top_Interview_150_Graph_General #2025_09_14_Time_38_ms_(86.28%)_Space_17.94_MB_(97.41%)

from typing import Dict, List, Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        return self._cloneGraph(node, {})

    def _cloneGraph(self, node: Optional[Node], processed_nodes: Dict[Node, Node]) -> Optional[Node]:
        if node is None:
            return None
        elif node in processed_nodes:
            return processed_nodes[node]
        new_node = Node()
        processed_nodes[node] = new_node
        new_node.val = node.val
        new_node.neighbors = []
        for neighbor in node.neighbors:
            cloned_neighbor = self._cloneGraph(neighbor, processed_nodes)
            if cloned_neighbor is not None:
                new_node.neighbors.append(cloned_neighbor)
        return new_node
