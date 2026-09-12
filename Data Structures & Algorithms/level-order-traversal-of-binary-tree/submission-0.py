# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root == None:
            return []
        queue.append(root)
        solution = []
        while(len(queue)>0):
            current_len = len(queue)
            current_sol = []
            while(current_len>0):
                current_element = queue.pop(0)
                current_sol.append(current_element.val)
                if current_element.left!= None:
                    queue.append(current_element.left)
                if current_element.right!= None:
                    queue.append(current_element.right)
                current_len-=1
            solution.append(current_sol)
        return solution

