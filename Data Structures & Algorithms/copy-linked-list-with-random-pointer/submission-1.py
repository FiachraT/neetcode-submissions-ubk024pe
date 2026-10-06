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
        node = head
        corresponding = {}

        while node:
            corresponding[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            corresponding[node].next = corresponding.get(node.next)
            corresponding[node].random = corresponding.get(node.random)
            node = node.next
        return corresponding.get(head)
        
     
        
        


        