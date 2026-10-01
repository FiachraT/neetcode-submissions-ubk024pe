# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #two pointers, if single (s) encounters double(s), then a cycle exists.
        # return true if single reaches the end of the list and has not encountered the loop
        if not head:
            return False
        s, d = head, head
        while d.next:
            s = s.next
            if d.next.next:
                d = d.next.next
                if s.val == d.val:
                    return True
            else:
                return False
        return False