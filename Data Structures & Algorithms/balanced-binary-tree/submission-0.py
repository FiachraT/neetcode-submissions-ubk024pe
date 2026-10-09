# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # only need to track true or false
        if not root:
            return True
        # abs(height of left - height of right) > 1: return False
        # need to return isBalnced and height, to return multple value, we return a list
        # return [isBalanced, height]
        def dfs(root: Optional[TreenNode]) -> list: 
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]



