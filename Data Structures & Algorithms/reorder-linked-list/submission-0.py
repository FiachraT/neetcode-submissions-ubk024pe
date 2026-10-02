# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         def rec(root: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
            #base case
            if not cur:
                return root
            # recursive case
            root = rec(root, cur.next) # cur goes to end, root stays root
            if not root:
                return None
            # first instance: root = 1, cur = 5
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp # root.next, so next is 3, 3
        

         if head:
            head = rec(head, head)




        