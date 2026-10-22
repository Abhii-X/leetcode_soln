'''

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5'''

Link:https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        def node(root,n):
            if root is None:
                return float('inf')
            if root.left is None and root.right is None:
                return n+1
            x=node(root.left,n+1)
            y=node(root.right,n+1)
            return min(x,y)
        if root is None:
            return 0
        return node(root,0)
