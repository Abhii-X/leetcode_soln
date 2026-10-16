'''

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]'''

Link:https://leetcode.com/problems/binary-tree-paths/description/

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        a=[]
        def path(root,s):
            if root is None:
                return
            s+=str(root.val)
            if root.left is None and root.right is None:
                a.append(s)
                return
            s+="->"
            path(root.left,s)
            path(root.right,s)
        path(root,"")
        return a
