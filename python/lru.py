class Node:
    """A doubly linked list node to store key-value pairs."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Stores key to node mapping
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """Add a node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Get the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)  # Move the accessed node to the front
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update the value of the key."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) >= self.capacity:
            # Remove the LRU from the cache and the list
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)

# Example usage:
lru = LRUCache(3)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
print(lru.get(1))  # Returns 1
lru.put(4, 4)  # Evicts key 2
print(lru.get(2))  # Returns -1 (not found)
print(lru.get(3))  # Returns 3
print(lru.get(4))  # Returns 4




