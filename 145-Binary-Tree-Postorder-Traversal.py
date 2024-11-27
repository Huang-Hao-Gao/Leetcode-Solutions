# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def walk(node):
            if node == None:
                return
            walk(node.left)
            walk(node.right)
            result.append(node.val)
        walk(root)
        return result
        
