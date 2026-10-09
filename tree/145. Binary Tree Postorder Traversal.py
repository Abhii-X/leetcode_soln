'''

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]'''

Link:https://leetcode.com/problems/binary-tree-postorder-traversal/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            a.append(root.val)
        postorder(root)
        return a
