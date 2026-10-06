"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(head.val, None, None)
        node = head
        new_node = new_head
        corresponding = {}
        corresponding[head] = new_head
        while node.next:
            new_node.next = Node(node.next.val, None, None)
            new_node = new_node.next
            node = node.next
            corresponding[node] = new_node
        # now new nodes have values and correct next values
        new_node = new_head
        node = head
        while new_node:
            if not node.random:
                new_node.random = None
            else:
                new_node.random = corresponding[node.random]
            new_node = new_node.next
            node = node.next
        return new_head
        
     
        
        


        