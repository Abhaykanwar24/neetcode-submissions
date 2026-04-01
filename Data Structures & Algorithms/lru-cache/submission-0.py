class Node:
    def __init__(self, key , value , nxt , prev):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0,None,None)
        self.right = Node(0,0,None,self.left)

        self.left.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]

            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            cur.next = self.right
            cur.prev = self.right.prev
            self.right.prev.next = cur
            self.right.prev = cur
            return cur.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur = self.cache[key]
            cur.value = value

            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        else:
            if self.cap == 0:
                # remove LRU (left.next)
                lru = self.left.next
                self.left.next = lru.next
                lru.next.prev = self.left
                del self.cache[lru.key]
                self.cap += 1

            cur = Node(key, value, self.right, self.right.prev)
            self.cache[key] = cur
            self.cap -= 1
        
        self.right.prev.next = cur
        cur.prev = self.right.prev
        cur.next = self.right
        self.right.prev = cur
