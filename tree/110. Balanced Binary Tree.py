'''


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true'''

Link:https://leetcode.com/problems/balanced-binary-tree/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0

            l = height(node.left)
            r = height(node.right)

            if l == -1 or r == -1:
                return -1

            if abs(l-r) > 1:
                return -1

            return max(l, r) + 1

        return height(root) != -1 
