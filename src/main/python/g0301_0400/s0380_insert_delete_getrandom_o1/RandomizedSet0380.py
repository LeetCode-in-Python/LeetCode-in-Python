# #Medium #Array #Hash_Table #Math #Design #Randomized #Programming_Skills_II_Day_20
# #Top_Interview_150_Array/String #2025_09_20_Time_90_ms_(96.69%)_Space_57.80_MB_(64.58%)

import random

class RandomizedSet:
    def __init__(self):
        self.map = {}   # value -> index
        self.list = []  # values

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        # Index of element to remove
        idx = self.map[val]
        last_val = self.list[-1]

        # Swap with last element
        self.list[idx] = last_val
        self.map[last_val] = idx

        # Remove last element
        self.list.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
