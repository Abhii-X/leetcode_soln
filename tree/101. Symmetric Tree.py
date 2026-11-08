'''
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false'''

Link:https://leetcode.com/problems/symmetric-tree/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        def check(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val!=r.val:
                return False
            return check(l.left,r.right) and check(l.right,r.left)
        return check(root.left,root.right)
