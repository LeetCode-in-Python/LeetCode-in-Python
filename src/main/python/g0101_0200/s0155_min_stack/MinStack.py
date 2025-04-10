# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Stack #Design
# #Data_Structure_II_Day_14_Stack_Queue #Programming_Skills_II_Day_18 #Level_2_Day_16_Design
# #Udemy_Design #Top_Interview_150_Stack #Big_O_Time_O(1)_Space_O(N)
# #2024_06_09_Time_58_ms_(38.23%)_Space_21_MB_(7.40%)

class MinStack:
    class Node:
        def __init__(self, min_val, data, previous_node=None, next_node=None):
            self.min = min_val
            self.data = data
            self.previous_node = previous_node
            self.next_node = next_node

    def __init__(self):
        self.current_node = None

    def push(self, val):
        if self.current_node is None:
            self.current_node = self.Node(val, val)
        else:
            self.current_node.next_node = self.Node(min(self.current_node.min, val), val, self.current_node)
            self.current_node = self.current_node.next_node

    def pop(self):
        self.current_node = self.current_node.previous_node

    def top(self):
        return self.current_node.data if self.current_node else None

    def getMin(self):
        return self.current_node.min if self.current_node else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
