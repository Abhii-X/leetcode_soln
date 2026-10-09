'''

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]'''

Link:https://leetcode.com/problems/binary-tree-inorder-traversal/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        inorder(root)
        return a
