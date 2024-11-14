# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #order:
        #left
        #value
        #right
       
        list = []
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            list.append(node.val)
            inorder(node.right)
        inorder(root)
        return list
        