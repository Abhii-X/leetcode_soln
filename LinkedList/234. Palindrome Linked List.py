'''

Example 1:


Input: head = [1,2,2,1]
Output: true

Example 2:


Input: head = [1,2]
Output: false'''

Link:https://leetcode.com/problems/palindrome-linked-list/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        a=[]
        curr=head
        while curr is not None:
            a.append(curr.val)
            curr=curr.next
        if a==a[::-1]:
            return True
        return False
