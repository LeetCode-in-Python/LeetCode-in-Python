146\. LRU Cache

Medium

Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

*   `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
*   `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
*   `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

**Input** ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

**Output:** [null, null, null, 1, null, -1, null, -1, 3, 4]

**Explanation:**

    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1); // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2); // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1); // return -1 (not found)
    lRUCache.get(3); // return 3
    lRUCache.get(4); // return 4 

**Constraints:**

*   `1 <= capacity <= 3000`
*   <code>0 <= key <= 10<sup>4</sup></code>
*   <code>0 <= value <= 10<sup>5</sup></code>
*   At most 2<code> * 10<sup>5</sup></code> calls will be made to `get` and `put`.

To solve the problem and implement the LRU Cache, we can use a combination of a dictionary (hash map) and a doubly linked list. This approach allows us to achieve O(1) time complexity for both the `get` and `put` operations.

### Steps:

1. **Define a Doubly Linked List Node**:
   - Define a class for the doubly linked list node with attributes `key`, `value`, `prev`, and `next`.

2. **Initialize the LRU Cache**:
   - Initialize the LRU cache with a dictionary to store key-value pairs and two dummy nodes for the head and tail of the doubly linked list.
   - Set `capacity` to the provided capacity.
   - Initialize a `size` variable to keep track of the number of elements in the cache.

3. **Implement `get` Operation**:
   - If the key exists in the cache, move the corresponding node to the front of the doubly linked list (indicating it was recently used) and return its value.
   - If the key does not exist, return -1.

4. **Implement `put` Operation**:
   - If the key exists in the cache, update its value and move the corresponding node to the front of the doubly linked list.
   - If the key does not exist:
     - If the cache is full (`size` equals `capacity`), remove the least recently used node (tail node) from the doubly linked list and the dictionary.
     - Create a new node with the provided key and value, add it to the front of the doubly linked list, and insert the key-value pair into the dictionary.
   - Update the `size` accordingly.

### Implementation:

```python
class LRUCache:
    class ListNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.ListNode()
        self.tail = self.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if self.size == self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove_node(self.tail.prev)
                self.size -= 1
            new_node = self.ListNode(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node
            self.size += 1
```

### Explanation:

1. **Define a Doubly Linked List Node**:
   - We define a nested class `ListNode` to represent nodes in the doubly linked list. Each node contains `key`, `value`, `prev`, and `next` attributes.

2. **Initialize the LRU Cache**:
   - In the `__init__` method, we initialize the LRU cache with the provided `capacity`, an empty dictionary `cache` to store key-value pairs, and two dummy nodes `head` and `tail` for the head and tail of the doubly linked list. We set `head.next` to `tail` and `tail.prev` to `head` to link them together. We also initialize `size` to 0.

3. **Implement `get` Operation**:
   - In the `get` method, if the key exists in the cache, we move the corresponding node to the front of the doubly linked list using the `_move_to_front` method and return its value. If the key does not exist, we return -1.

4. **Implement `put` Operation**:
   - In the `put` method, if the key exists in the cache, we update its value and move the corresponding node to the front of the doubly linked list. If the key does not exist:
     - If the cache is full, we remove the least recently used node (tail node) from the doubly linked list and the dictionary.
     - We create a new node with the provided key and value, add it to the front of the doubly linked list, and insert the key-value pair into the dictionary.
   - We update the `size` accordingly.

This implementation ensures that both `get` and `put` operations run in O(1) average time complexity.