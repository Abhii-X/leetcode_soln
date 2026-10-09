'''

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]'''

Link:https://leetcode.com/problems/binary-tree-preorder-traversal/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def preorder(root):
            if root is None:
                return None
            a.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return a
