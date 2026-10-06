# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 and l2 non negate integer lists
        # 360 + 560 = 920
        # 0, 6, 3 + 0, 6, 5 = 0, 2, 9
        # lists are non empty but they could be different lengths

        carry = 0
        dummy = ListNode()
        node = dummy
        while l1 or l2 or carry:
            if l1: val1 = l1.val
            else: val1 = 0
            if l2: val2 = l2.val
            else: val2 = 0
            num = val1 + val2 + carry
            carry = 0
            if num >= 10:
                num = num % 10
                carry = 1
            node.next = ListNode(num)
            node = node.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

            

        