'''

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []'''

Link:https://leetcode.com/problems/binary-tree-level-order-traversal/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        a=[]
        d=deque([root])
        while d:
            s=len(d)
            b=[]
            for i in range(s):
                x=d.popleft()
                b.append(x.val)
                if x.left:
                    d.append(x.left)
                if x.right:
                    d.append(x.right)
            a.append(b)
        return a
