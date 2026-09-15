# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append(root)
        if root == None:
            return []
        solution = []
        while(len(queue)>0):
            current_size = len(queue)
            current_level = []
            while(current_size):
                current_node = queue.pop(0)
                current_level.append(current_node.val)
                if current_node.left!=None:
                    queue.append(current_node.left)
                if current_node.right!=None:
                    queue.append(current_node.right)
                current_size -=1
            solution.append(current_level[-1])
        return solution

