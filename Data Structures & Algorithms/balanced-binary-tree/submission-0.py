# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.notBalanced = False
        def dfs(current):
            if current == None:
                return 0
                
            left = dfs(current.left)
            right = dfs(current.right)
            if abs(left-right)>1:
                self.notBalanced = True
            return 1 + max(left,right)
        dfs(root)
        if self.notBalanced:
            return False
        return True

