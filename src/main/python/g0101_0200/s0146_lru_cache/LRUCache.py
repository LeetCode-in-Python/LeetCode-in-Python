# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Hash_Table #Design #Linked_List
# #Doubly_Linked_List #Udemy_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(1)_Space_O(capacity) #2025_07_25_Time_113_ms_(84.08%)_Space_77.93_MB_(87.77%)

class LRUCacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            self.move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            node = self.cache_map[key]
            node.value = value
            self.move_to_head(node)
        else:
            if len(self.cache_map) < self.capacity:
                node = LRUCacheNode(key, value)
                self.cache_map[key] = node
                if not self.head:
                    self.head = node
                    self.tail = node
                else:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
            else:
                last = self.tail
                if last:
                    self.tail = last.prev
                    if self.tail:
                        self.tail.next = None
                    self.cache_map.pop(last.key)
                    if not self.cache_map:
                        self.head = None
                self.put(key, value)

    def move_to_head(self, node: LRUCacheNode) -> None:
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
