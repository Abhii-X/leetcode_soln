'''

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.'''

Link:https://leetcode.com/problems/middle-of-the-linked-list/description/

#Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        a=[]
        curr=head
        while curr is not None:
            a.append(curr.val)
            curr=curr.next
        print(a)
        b=len(a)//2
        c=[]
        for i in range(b,len(a)):
            c.append(a[i])
        print(c)
        root =None
        tail=None
        for i in range(len(c)):
            new_node=ListNode(c[i])
            if root is None:
                root=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=tail.next
        return root
