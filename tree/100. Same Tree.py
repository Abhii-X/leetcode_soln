'''

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false'''

Link:https://leetcode.com/problems/same-tree/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def same(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            l=same(p.left,q.left)
            r=same(p.right,q.right)
            return l and r
        return same(p,q)
