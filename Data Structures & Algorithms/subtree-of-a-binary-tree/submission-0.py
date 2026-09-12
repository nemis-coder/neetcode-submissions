# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        if p == None and q==None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        elif p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates_roots = []
        target = subRoot.val
        def dfs(root,target):
            if root == None:
                return
            if root.val == target: 
                candidates_roots.append(root)
            dfs(root.left, target)
            dfs(root.right, target)
        dfs(root, target)
        for candidate in candidates_roots:
            if self.isSameTree(subRoot, candidate):
                return True
        return False


            