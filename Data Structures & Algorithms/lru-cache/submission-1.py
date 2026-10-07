class Node:
      def __init__ (self, key: int, val: int ) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    ## should map what is stored and the sequence number
    ## sequence number should keep going up, remove smallest sequence number

    def __init__(self, capacity: int):
        self.capacity = capacity # capacity = length
        self.cache = {} # map key to node
        self.d_head, self.d_tail = Node(0, 0), Node(0,0)
        self.d_head.next, self.d_tail.prev = self.d_tail, self.d_head
        
   #have to update that it has been recently used
   #map = key: int, doubly linked list, last thing accessed moves to the rightmost end of the list
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            return

        if len(self.cache) >= self.capacity:
            lru = self.d_head.next
            self.remove(lru) 
            del self.cache[lru.key]

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        

    def insert(self, node):
        prv, nxt = self.d_tail.prev, self.d_tail
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt



    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    


        
