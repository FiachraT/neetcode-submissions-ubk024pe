# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #turn all lefts to rights and rights to lefts
        if not root:
            return 
        
        def invert(root: Optional[TreeNode], cur: Optional[TreeNode]):
            if not cur:
                return root
            root = invert(root, cur.left)
            root =invert(root, cur.right)
            cur.left, cur.right = cur.right, cur.left
            return root
        
        root = invert(root, root)
        return root
        
        