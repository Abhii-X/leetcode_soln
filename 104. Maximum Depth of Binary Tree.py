'''

Explanation:

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

 Example:

 Input: root = [3,9,20,null,null,15,7]
Output: 3'''

Link:https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def node(root, count):
            if root is None:
                return count
            left=node(root.left,count+1)
            right=node(root.right,count+1)
            return max(left,right)
        if root is None:
            return 0
        return node(root,0)
