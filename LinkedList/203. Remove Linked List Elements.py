'''
Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

Link:https://leetcode.com/problems/remove-linked-list-elements/description/'''

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        root=head
        a=[]
        while root is not None:
            if root.val!=val:
                a.append(root.val)
            root=root.next
        print(a)
        temp=None
        tail=None
        for i in range(len(a)):
            new_Node=ListNode(a[i])
            if temp is None:
                temp=new_Node
                tail=new_Node
            else:
                tail.next=new_Node
                tail=tail.next
        return temp
