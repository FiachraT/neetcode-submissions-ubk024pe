# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reorder(root, cur):
            if not cur:
                return root
            
            root = reorder(root, cur.next)
            if not root:
                return None
            # after first base case hit, root = 0, cur =6
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp
    

        head = reorder(head, head.next)

        