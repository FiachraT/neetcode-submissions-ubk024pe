# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        l = count - n - 1
        if l < 0:
            return head.next
        cur = head
        while l > 0:
            cur = cur.next
            l -= 1
        if cur and cur.next:
            cur.next = cur.next.next
        return head
        
        