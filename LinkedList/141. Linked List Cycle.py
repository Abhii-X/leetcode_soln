'''

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.'''

Link:https://leetcode.com/problems/linked-list-cycle/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        temp=head
        while temp:
            if temp.next not in a:
                a.add(temp.next)
                temp=temp.next
            else:
                return True
                break
        return False
