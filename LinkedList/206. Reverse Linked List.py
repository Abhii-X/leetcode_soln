'''
Example:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]'''


#Link:https://leetcode.com/problems/reverse-linked-list/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        curr=head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
