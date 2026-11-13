'''

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []'''

Link:https://leetcode.com/problems/sort-list/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        a=[]
        curr=head
        while curr is not None:
            a.append(curr.val)
            curr=curr.next
        b=sorted(a)
        print(b)
        root=None
        tail=None
        for i in range(len(b)):
            new_Node=ListNode(b[i])
            if root is None:
                root=new_Node
                tail=new_Node
            else:
                tail.next=new_Node
                tail=tail.next
        return root
