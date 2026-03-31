from typing import List

class LinkedList:

    class Node:

        def __init__(self, val: int):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while node:
            if i == index:
                return node.val
            node = node.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        new_head = LinkedList.Node(val)
        new_head.next = self.head
        self.head = new_head
        
    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = LinkedList.Node(val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = LinkedList.Node(val)
        
    def remove(self, index: int) -> bool:
        #need to asign the node before the indexed node's next to the indexed node next
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        node = self.head
        index = index - 1
        i = 0
        while node.next:
            if i == index:
                node.next = node.next.next
                return True
            node = node.next
            i +=1
        return False


    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node:
            values.append(node.val)
            node = node.next
        return values

        
